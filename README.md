# 🧠 Free AI Leetcode Solver by [algorithmspath.com](https://algorithmspath.com/)

> *“Screw grinding. Bring the AI.”*

Welcome to the **Free AI Leetcode Solver** – a brutally honest, cheeky, and wickedly effective screenshot-to-solution tool, crafted for the modern coding warrior who's tired of gatekept grind culture.

Whether you're:

* A student drowning in DSA homework
* A 9-to-5-er too fried to reverse a linked list after hours
* A job seeker disillusioned by technical interviews that feel more like memory tests
* Or someone who's ever looked at a Leetcode Hard and quietly shut the tab...

This tool is for  **you** .

### 🤖 What It Does (In Human Terms)

With a single screenshot and your LLM API key, you can:

* 📸 Snap a coding problem
* 🧠 Let our tool decode it with OCR + LLM magic
* ✨ Get a working solution and explanation

All on your local machine. No logins. No data leaks. No BS.

---

## 🚀 Key Features

* 📷  **Screenshot to Solution** : Just take a screenshot — it does the rest.
* 🤖  **LLM-Powered Brains** : Plug in GPT-4o, Gemini, Claude, Mistral, DeepSeek, or your favorite large language model.
* 🧠  **Multi-Platform Support** : Works with problems from Leetcode, GeeksForGeeks, Codeforces, HackerRank, and more.
* 🔍  **Understands More Than Just Text** : Diagrams? Code snippets? Paragraphs of explanation? Bring it on.
* 💬  **Explanations That Actually Explain** : Not just answers — structured breakdowns and reasoning.
* 🔒  **Privacy First** : Local-first execution. Your API keys and screenshots never touch the cloud.
* 💻  **Currently for Windows** : macOS & Linux coming soon (PRs welcome!).

---

## 🖥️ Compatibility

| Supported Platforms                                                                                                                                                                                                                                             | Supported LLMs                                                                                                                                                                                                                                                                                                    | OS Support                                                                                                                                 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| ![Leetcode](https://img.shields.io/badge/Leetcode-orange?logo=leetcode) ![GFG](https://img.shields.io/badge/GeeksForGeeks-28a745?logo=data:image/png;base64,iVBOR...) ![Codeforces](https://img.shields.io/badge/Codeforces-blue?logo=data:image/png;base64,iVBOR...) | ![OpenAI](https://img.shields.io/badge/OpenAI-API-black?logo=openai) ![Gemini](https://img.shields.io/badge/Gemini-Google-blue?logo=google) ![Claude](https://img.shields.io/badge/Claude-Anthropic-7c4dff?logo=anthropic) ![Mistral](https://img.shields.io/badge/Mistral-AI-ffcc00?logo=data:image/png;base64,iVBOR...) | ![Windows](https://img.shields.io/badge/Windows-OS-blue?logo=windows) ![macOS](https://img.shields.io/badge/macOS-coming_soon-grey?logo=apple) |

> *Note: Badge rendering works beautifully in GitHub markdown previews.*

---

## 📦 Installation Guide (Windows Only for Now)

> *Linux/macOS users – we see you. Support is on the way.*

1. Clone the repo:

```bash
git clone https://github.com/algorithmspath-com/free-ai-leetcode-solver.git
cd free-ai-leetcode-solver
```

2. Navigate to the executable directory:

```
exe/
└── win/
    ├── AssistServer/        # Backend engine
    ├── Tesseract/           # OCR magic
    └── free-ai-leetcode-solver.exe  # Launcher
```

3. Launch the `.exe` file
4. Paste your API key (OpenAI, Gemini, etc.)
5. Press that screenshot hotkey → receive your solution

---

## 🔬 How It Works (Under the Hood)

Here's a peek at the internals:

* **AssistServer** : Receives the screenshot and orchestrates the flow
* **Tesseract** : Runs OCR to extract raw text from the image
* **LLM API Call** : Sends structured prompts to your chosen language model
* **Output** : Clean code, explanations, and optionally further insights

🔐 Everything runs locally. No screenshot or key ever leaves your machine.

---

## ✨ Philosophy: Why This Exists

We didn’t want to build another "grind 5 problems daily to get a badge" platform. Those already exist. Some are great. Most feel like productivity cosplay.

Instead, we built this for that *exact* moment when you hit cognitive burnout, the problem looks like ancient alien math, and you whisper:

> *“Screw it. Let’s see what the AI says.”*

And guess what? That’s okay. This isn’t cheating. It’s  **augmenting** . It’s  **learning smartly** . It’s  **preserving your energy for what matters** .

Inspired by the glorious final seconds of [this video](https://www.youtube.com/watch?v=c_KuqYVDpJg):

> *“…and then he pulled out his AI.”*

---

## 🙋 Need Help?

Got questions or feedback?

* Email: [support@algorithmspath.com](mailto:support@algorithmspath.com)
* Open an issue / start a discussion on GitHub

---

## 🔑 LLM API Key Tips

Make sure:

* You're using a valid key (e.g., starts with `sk-` for OpenAI)
* You've selected a supported model in your settings
* You’ve got available quota/credits

If it’s not working:

* Restart the app
* Check the logs
* Reach out if you’re stuck — we’re happy to help!

---

## 🛠 Contribute

We’re early — and that means wide open for collaboration.
Want to:

* Add macOS/Linux support?
* Integrate a new model?
* Refine the UI?
* Translate it?

Jump in:

1. Fork the repo
2. Create a feature branch
3. Submit a PR

---

## 📄 License

This project is licensed under  **AGPL-3.0** .

That means:

* It’s free
* You can use, remix, and redistribute it
* But if you ship changes — **you must share your code**

Let the AIs help you. But keep the spirit open source ✊
