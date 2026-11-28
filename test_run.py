import os
from agents.requirements import requirement_gatherer
from agents.design import design_agent

result=requirement_gatherer.run("a simple calculator")

os.makedirs("workspace",exist_ok=True)
with open("workspace/spec.md","w",encoding="utf-8") as f:
    f.write(result)

print("saved to workspace")

with open("workspace/spec.md","r",encoding="utf-8") as f:
    data=f.read()

design=design_agent.run(data)

with open("workspace/design.md","w",encoding="utf-8") as f:
    f.write(design)