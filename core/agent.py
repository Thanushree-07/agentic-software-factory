
from groq import Groq
import json
import os
class Agent:
    def __init__(self,name,role,system_prompt):
        self.name=name
        self.role=role
        self.system_prompt=system_prompt
        self.client=Groq(api_key=os.getenv("GROQ_API_KEY"))

    def run(self,user_input):
        messages=[
            {
                "role":"system",
                "content":self.system_prompt
            },
            {
                "role":"user",
                "content":user_input
            }

        ]

        
        response=self.client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages,
            temperature=0.2,
            

        )
        return response.choices[0].message.content