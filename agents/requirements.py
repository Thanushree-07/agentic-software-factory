from core.agent import Agent

requirement_gatherer=Agent(name="reuirement writer",role="gather annd list down the requirements",system_prompt="you are requirement gatherer to users context.list down requiremensts need to accomplish users task .dont make it too big though.")
result=requirement_gatherer.run("give me requirements for building a multi agent coding system")
print(result)