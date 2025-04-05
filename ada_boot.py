#!/usr/bin/env python3
import os, subprocess, argparse

AGENCY_PATH = os.path.expanduser("~/ADA_AGENCY")

AGENTS = {
    "watch": "d.agent.py",
    "video": "video_agent.py",
    "model": "m.agent.py",
    "sync": "sync.agent.sh",
    "task": "task_center.py"  # placeholder for future drop
}

def run_agent(agent, extra_args=None):
    file = os.path.join(AGENCY_PATH, AGENTS[agent])
    if not os.path.exists(file):
        print(f"❌ Agent not found: {file}")
        return
    cmd = ["python3", file] if file.endswith(".py") else [file]
    if extra_args:
        cmd += extra_args
    subprocess.run(cmd)

def main():
    parser = argparse.ArgumentParser(description="🚀 ADA AGENT CLI BOOT")
    parser.add_argument("--watch", action="store_true", help="Run clipboard/folder watcher")
    parser.add_argument("--video", action="store_true", help="Trigger video agent")
    parser.add_argument("--model", nargs=argparse.REMAINDER, help="Send to multi-model router")
    parser.add_argument("--sync", action="store_true", help="Push to GitHub")
    parser.add_argument("--task", nargs=argparse.REMAINDER, help="Run a task by keyword")

    args = parser.parse_args()

    if args.watch:
        run_agent("watch")
    elif args.video:
        run_agent("video")
    elif args.model:
        run_agent("model", args.model)
    elif args.sync:
        run_agent("sync")
    elif args.task:
        run_agent("task", args.task)
    else:
        print("⚙️ Usage: ada --watch | --video | --model 'prompt' | --sync | --task 'name'")

if __name__ == "__main__":
    main()

