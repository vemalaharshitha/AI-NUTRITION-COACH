import json
import tempfile
import gradio as gr
from gtts import gTTS
import random
import requests

# ================= MODE SWITCH =================
USE_API = False  # keeps project SAFE while API code is visible
API_KEY = "paste_your_api_key"
MODEL = "gemini-2.0-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

# ================= CHAT HISTORY =================
chat_history = []

# ================= SMART OFFLINE RESPONSES =================
def offline_smart_reply(message):

    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! I'm your AI nutrition coach. What's your health goal?"
    
    if "weight" in message and "lose" in message:
        return "Great goal! How much do you currently weigh and what's your target?"

    if "gain" in message:
        return "Got it! To gain healthy weight, I need to know about your meals. What do you usually eat?"

    if "vegetarian" in message:
        return "Nice! I can help with vegetarian meal plans. Do you prefer simple or detailed diet plans?"

    if "diet" in message or "plan" in message:
        return (
            "Here is a simple healthy diet plan:\n\n"
            "🌅 **Breakfast:** Oats / Idli / Upma + Fruit\n"
            "🍱 **Lunch:** 2 Chapatis + Dal + Vegetables + Salad\n"
            "🍎 **Snacks:** Fruits / Nuts\n"
            "🌙 **Dinner:** Light roti + Veg curry / soups\n\n"
            "Would you like a personalized plan?"
        )

    if "allergy" in message:
        return "Thanks! Please tell me what kind of allergies you have."

    if "rice" in message or "chapati" in message:
        return "Got it. I can balance your meals with rice/chapati. Do you exercise regularly?"

    # fallback
    return random.choice([
        "That's interesting! Tell me more.",
        "Okay, can you explain slightly more?",
        "Sure! What is your height and weight?",
        "I'm here to help. Continue..."
    ])

# ================= REAL GEMINI MODE (if USE_API=True) =================
def ask_gemini_online(question):
    try:
        chat_history.append({"role": "user", "content": question})

        data = {
            "contents": [
                {"parts": [{"text": entry["content"]} for entry in chat_history]}
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": API_KEY
        }

        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        result = response.json()

        reply_text = result["candidates"][0]["content"]["parts"][0]["text"]
        chat_history.append({"role": "assistant", "content": reply_text})
        return reply_text

    except:
        return "(Offline fallback active due to API issue)"

# ================= MAIN ROUTING =================
def get_reply(message):
    if USE_API:
        return ask_gemini_online(message)
    else:
        return offline_smart_reply(message)

# ================= TEXT TO SPEECH =================
def speak(text):
    tts = gTTS(text)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    tts.save(tmp.name)
    return tmp.name

# ================= BMI CALCULATOR =================
def calculate_bmi(height_cm, weight_kg):
    try:
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal weight" if bmi < 25 else
            "Overweight" if bmi < 30 else
            "Obese"
        )
        return f"Your BMI is {bmi:.2f} — {category}"
    except:
        return "Enter valid numbers."

# ================= CHAT LOGIC =================
def respond(user_message, history):
    bot_reply = get_reply(user_message)

    history = history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": bot_reply}
    ]

    audio_path = speak(bot_reply)
    return "", history, audio_path

# ================= UI =================
with gr.Blocks() as demo:

    gr.Markdown("<h1 style='text-align: center; color:#4b5cff;'>✨ Nurture : Your AI Nutrition Coach ✨</h1>")
    gr.Markdown("<p style='text-align:center;'>Smart diet guidance • BMI calculator • Voice output</p>")

    with gr.Row():

        with gr.Column(scale=2):
            chatbot = gr.Chatbot(label="Chat with Nurture", height=350)

            message = gr.Textbox(label="Your Message", placeholder="Ask something...")
            send_btn = gr.Button("Send", variant="primary")

            audio_output = gr.Audio(label="AI Voice", type="filepath")

            send_btn.click(
                respond,
                inputs=[message, chatbot],
                outputs=[message, chatbot, audio_output]
            )

        with gr.Column(scale=1):
            gr.Markdown("### 🧮 BMI Calculator")

            height = gr.Number(label="Height (in cm)")
            weight = gr.Number(label="Weight (in kg)")
            bmi_output = gr.Textbox(label="Your BMI Result")
            bmi_btn = gr.Button("Calculate BMI", variant="secondary")

            bmi_btn.click(
                calculate_bmi,
                inputs=[height, weight],
                outputs=bmi_output
            )

demo.launch(share=True, theme=gr.themes.Soft())
