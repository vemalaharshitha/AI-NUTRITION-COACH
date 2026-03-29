# 🥗 Nurture – AI Nutrition Coach

✨ *Smart Diet Guidance • BMI Calculator • Voice Assistant*

---

## 📌 Overview

**Nurture** is an AI-powered nutrition assistant built using **Gradio**, **gTTS**, and intelligent response logic.
It helps users improve their health through diet suggestions, BMI analysis, and interactive chat support.

---

## 🚀 Features

* 💬 **AI Chat Assistant**

  * Provides diet advice and health guidance
  * Works in both offline and online (API) modes

* 🧮 **BMI Calculator**

  * Calculates Body Mass Index
  * Gives health category (Underweight, Normal, Overweight, Obese)

* 🔊 **Voice Output**

  * Converts AI responses into speech using gTTS

* 🥦 **Diet Recommendations**

  * Suggests healthy meal plans
  * Supports vegetarian preferences

* ⚡ **Offline Smart Mode**

  * Works without internet using predefined intelligent responses

---

## 🛠️ Tech Stack

* **Frontend/UI:** Gradio
* **Backend Logic:** Python
* **Text-to-Speech:** gTTS (Google Text-to-Speech)
* **API (Optional):** Google Gemini API

---

## 📂 Project Structure

```
📁 Nurture-AI-Nutrition-Coach
│── app.py
│── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/nurture-ai.git
cd nurture-ai
```

### 2. Install dependencies

```bash
pip install gradio gtts requests
```

### 3. Run the application

```bash
python app.py
```

---

## 🌐 Usage

* Open the local URL shown in terminal (e.g., `http://127.0.0.1:7860`)
* Chat with the AI nutrition coach
* Calculate BMI
* Listen to AI responses via voice output

---

## 🔄 Modes

| Mode       | Description                       |
| ---------- | --------------------------------- |
| Offline    | Uses smart predefined responses   |
| Online API | Uses Gemini AI for real responses |

To enable API mode:

```python
USE_API = True
```

---

## 📊 Example Features

* Ask: *"Give me a diet plan"*

* Get: Structured healthy meal plan

* Input: Height & Weight

* Output: BMI + Health category

---

## 🎯 Future Enhancements

* 🌍 Multi-language support
* 📱 Mobile-friendly UI improvements
* 🧠 Advanced AI diet personalization
* 📈 Health tracking dashboard

---

## 👩‍💻 Author

**Harshitha**
💡 Passionate about AI, UI/UX, and building real-world applications

---

## ⭐ Contribute

Feel free to fork this repo and improve it!
Pull requests are welcome 🚀

---

## 📜 License

This project is open-source and available under the **MIT License**.

---
