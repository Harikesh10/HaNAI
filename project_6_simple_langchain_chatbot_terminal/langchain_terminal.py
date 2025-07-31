from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"

def langchain_chatbot_terminal():
    llm = ChatGoogleGenerativeAI(model= model , google_api_key= google_api_key)
    print("Powerful AI by a noob learner")
    while(True):
        user_input = input("User:")
        if user_input.lower() =="q":
            break
        response = llm.invoke(user_input)
        print(f"Jarvis:{response.content}")
langchain_chatbot_terminal()

