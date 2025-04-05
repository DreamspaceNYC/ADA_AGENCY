#!/bin/bash
cd ~/ADA_AGENCY
msg="🔁 AutoSync: $(date '+%Y-%m-%d %H:%M:%S')"
git add .
git commit -m "$msg"
git push
echo "$msg" >> ada_memory.log

