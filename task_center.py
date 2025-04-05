#!/usr/bin/env python3
import sys, json, os
from datetime import datetime

DATA_PATH = "task_center.json"
LOG_PATH = "ada_memory.log"

def log(msg):
    with open(LOG_PATH, "a") as f:
        f.write(f"{datetime.now()} | [task_center] {msg}\n")

def load_tasks():
    if not os.path.exists(DATA_PATH):
        return {"tasks": [], "agents": [], "ideas": []}
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_tasks(data):
    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)

def list_tasks(data):
    print("\n🧠 Tasks:")
    for i, t in enumerate(data["tasks"], 1):
        print(f"{i}. {t}")
    print("\n💡 Ideas:")
    for i, idea in enumerate(data["ideas"], 1):
        print(f"{i}. {idea}")
    print("\n🛠 Agents:")
    for i, a in enumerate(data["agents"], 1):
        print(f"{i}. {a}")

def add_entry(data, entry, key):
    data[key].append(entry)
    log(f"Added to {key}: {entry}")
    print(f"✅ Added to {key}.")

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage:\n  task_center.py list\n  task_center.py add task 'Write a sync agent'\n  task_center.py add idea 'Auto-transcribe YouTube'\n")
        return

    data = load_tasks()
    cmd = args[0]

    if cmd == "list":
        list_tasks(data)
    elif cmd == "add" and len(args) >= 3:
        _, key, content = args[0], args[1], " ".join(args[2:])
        if key in ["tasks", "ideas", "agents"]:
            add_entry(data, content, key)
            save_tasks(data)
        else:
            print("❌ Invalid key. Use: tasks, ideas, agents")
    else:
        print("⚠️ Unknown command or wrong usage.")

if __name__ == "__main__":
    main()
