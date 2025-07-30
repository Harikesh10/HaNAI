#load libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

#load the env variable
load_dotenv()
# load the necessary links
api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash"
base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"

 
client = OpenAI(base_url = base_url , api_key = api_key)
#get the data from the txt document
url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
response = requests.get(url)

#Get the file (rag.py , the file's directory)
script_dir = os.path.dirname(os.path.abspath(__file__))
# print(script_dir)
file_path = os.path.join(script_dir,"herenowai.txt")
#get the text content from the url, and crete a empty file and write the content in the file
with open(file_path,"wb") as file:
    file.write(response.content)
text = file_path
#to catch the errors
#When the text is entered it is encoded as number and fed to the llm , this is only understood by the llm
try:
    with open(text,"r",encoding="utf-8") as f:
        text_line = f.readlines()
        text_context = "\n".join ([line.strip() for line in text_line if line.strip()])
except Exception as e:
    print(f"Error{e}")
    text_context = "Error from extracting the text content"
    
def rag_bot(message,history):
    system_prompt =f"""You are the personal assitant built by Hari. Answer my questions only on the following context: \n\n{text_context}"""
    messages = [{"role":"system","content":system_prompt}]
    messages.extend(history)
    messages.append({"role":"user","content":message})
    response = client.chat.completions.create(model=model,messages = messages)
    ai_response = response.choices[0].message.content
    return ai_response

print(rag_bot("Who is the ceo of here and now ai?",[]))