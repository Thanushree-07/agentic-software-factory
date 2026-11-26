from agent import Agent

requirement_gatherer=Agent(name="reuirement writer",role="gather annd list down the requirements",system_prompt="gather and list down requirements given my users task")
result=requirement_gatherer.run("give me requirements for building a multi agent coding system")
print(result)