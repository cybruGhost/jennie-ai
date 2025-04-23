
---

# JENNIE AI — Terminal Virtual Assistant

**Jennie AI** is your smart, speaking terminal assistant built with **Python**. She can answer questions using **predefined data**, search the **web via Wikipedia**, perform **calculations**, and **speak back** to you — all from the comfort of your terminal.

---

## ⭐ Features

- **Predefined intelligence**: Instant responses from a built-in knowledge set
- **Wikipedia integration**: Fetch summaries and info live from Wikipedia
- **Math wizard**: Solve basic arithmetic and logic-based problems
- **Voice output**: She speaks! Using text-to-speech to talk back
- **Simple terminal interface**: Lightweight, no GUI needed

---

## 🧠 How It Works

- Text input from the user
- Matched against a predefined dictionary of intents
- If no match is found: searches Wikipedia
- If mathematical input is detected: evaluates and returns results
- Converts text responses to speech using a TTS engine (like `pyttsx3`)

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/cybruGhost/jennie-ai.git
cd jennie-ai

2. Install Required Dependencies

pip install -r requirements.txt

> If you run into any errors, open ChatGPT and ask:

"How do I fix dependency errors for Jennie AI Python project?"



3. Run Jennie

python jennie-ai.py

Jennie will greet you and wait for your questions.


---

✨ Sample Commands

Who is Albert Einstein?

What is the capital of Kenya?

20 + (30 / 2)

Define quantum mechanics

Hello Jennie


She responds with voice and text.


---

📦 Dependencies

pyttsx3 — for text-to-speech

wikipedia — for live knowledge

datetime, os, sys, math, re — for utilities and parsing



---

🔐 Privacy

Jennie runs completely offline unless Wikipedia is queried. No data is collected, logged, or stored.


---

🛠 Troubleshooting

If you get an error:

1. Check your Python version (recommended: Python 3.8+)


2. Run pip install -r requirements.txt again


3. If still stuck, copy the error and paste it into ChatGPT — it’s got your back




---

🪪 License

MIT License — because good AI should be open and ethical.

> Created by Cubic Company
"Jennie speaks, so you don’t have to search."



Let me know if you want to add cool terminal effects like typing animations or colors!

