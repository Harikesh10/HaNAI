#Import the necessary libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
from prompt import ai_chef 
#load the variable from .env file
load_dotenv()
#Import the neccessary model , api
api_key = os.getenv("GEMINI_API_KEY")
model="gemini-2.5-flash"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
client = OpenAI(base_url = base_url, api_key = api_key)
#System prompt for rules of response
#--> Reduce lines
ai_chef = ai_chef

def get_response(message,history):
    messages = [{"role":"system","content":ai_chef}]
    messages.extend(history)
    messages.append({"role":"user","content":message})
    response = client.chat.completions.create(model=model,messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response 


while(True):
    output = input()
    print(get_response(output,[]))