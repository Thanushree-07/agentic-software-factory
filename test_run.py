import os
from agents.requirements import requirement_gatherer

result=requirement_gatherer.run("an AI codinf assistant")

os.makedirs("workspace",exist_ok=True)
with open("workspace/spec.md","w",encoding="utf-8") as f:
    f.write(result)

print("saved to workspace")

