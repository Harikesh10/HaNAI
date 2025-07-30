#import the libraries
from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import PyPDF2
load_dotenv()
#load the necessary stuff
api_key = os.getenv("GEMINI_API_KEY")
base_url = "https://generativelanguage.googleapis.com/v1beta/openai"
model = "gemini-2.5-flash"
client = OpenAI(base_url = base_url , api_key = api_key)
#fetch the pdf 
url = "https://raw.githubusercontent.com/hereandnowai/sathyabama-be-cse-ai-pt1-07-2025-hands-on-professional-training-on-genai-and-ai-agents/main/general-profile-of-hereandnowai.pdf"
response = requests.get(url)
#create the pdf
PDF_FILE_NAME = "profile_hereandnowai.pdf"
PDF_DIR = os.path.dirname(__file__)
# print(PDF_DIR)
PDF_PATH = os.path.join(PDF_DIR,PDF_FILE_NAME)
# print(PDF_PATH)
#Write the pdf
with open(PDF_PATH,"wb") as file:
    file.write(response.content)
#Check for error, by reading the pdf
try:
    #reading the pdf and creating chunks for better processing
    with open(PDF_PATH,"rb") as f:
        reader = PyPDF2.PdfReader(f)
        pdf_text_chunks = []
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                pdf_text_chunks.append(page_text.strip())
        pdf_context ="\n".join(pdf_text_chunks) if pdf_text_chunks else "No Text found in pdf"
except Exception as e:
    print(f"Error reading pdf: {e}")
    pdf_context="Error when extracting in pdf"
    


def pdf_ragbot(message,history):
    system_prompt = f"""Context from{PDF_PATH}:\n{pdf_context}\n\n Question:{message}\n\n Answer based only on the context: """
    messages =[{"role":"system","content":system_prompt}]
    messages.extend(history)
    messages.append({"role":"user","content":message})
    response = client.chat.completions.create(model = model , messages = messages)
    ai_response = response.choices[0].message.content
    return ai_response 

print(pdf_ragbot("What is the slogan for here and now ai",[]))


