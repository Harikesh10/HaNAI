#Import the necc libraries
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
#load the important links
load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash-lite"
#The system
def run_langchain():
    """
    Instantiates a ChatGoogleGeneratiev AI model
    Invoke it with a simple prompt
    Prints the model's response
    """
    llm =ChatGoogleGenerativeAI(model=model, google_api_key = google_api_key)
    response = llm.invoke("Explain generative AI to kid in 3 lines")
    print(response.content)
run_langchain()




