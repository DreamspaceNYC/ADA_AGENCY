#!/usr/bin/env python3
import sys, os, openai, json
from datetime import datetime
from dotenv import load_dotenv

# === Load Environment ===
load_dotenv()
LOG = "ada_memory.log"
CONFIG_PATH = ".config.json"

def log(msg):
    with open(LOG, "a") as f:
        f.write(f"{datetime.now()} | [m.agent] {msg}\n")

def choose_model(prompt):
    if "explain" in prompt or "analyze" in prompt:
        return "openrouter/anthropic/claude-3-opus"
    elif "code" in prompt or "refactor" in prompt or "fix":
        return "openrouter/openai/gpt-4o"
    elif "summarize" in prompt or "draft":
        return "openrouter/meta-llama/llama-3-70b-instruct"
    else:
        return "openrouter/mistralai/mixtral-8x7b"

def ask_model(prompt, model):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_base = os.getenv("OPENAI_API_BASE", "https://openrouter.ai/api/v1")

    log(f"⚙️ Sending to model: {model}")
    try:
        res = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        output = res.choices[0].message.content
        log(f"✅ Response: {output[:100]}...")
        print("\n💬", output)
    except Exception as e:
        log(f"❌ Error: {e}")
        print("⚠️ Error:", e)

def main():
    prompt = " ".join(sys.argv[1:])
    if not prompt:
        print("Usage: m.agent <your prompt>")
        return
    model = choose_model(prompt)
    ask_model(prompt, model)

if __name__ == "__main__":
    main()

