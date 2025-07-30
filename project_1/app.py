# Import necessary libraries
from openai import OpenAI
import os
from dotenv import load_dotenv # Load environment variables
# from google.colab import userdata

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with Gemini API key
# Make sure to replace 'GEMINI_API_KEY' with your actual API key
api_key = os.getenv("GEMINI_API_KEY")
base_url="https://generativelanguage.googleapis.com/v1beta/openai"

# Configure OpenAI client for VS Code environment
client = OpenAI(base_url=base_url, api_key=api_key)

# Configure OpenAI client for Colab environment (commented out)
# client = OpenAI(api_key=userdata.get("GOOGLE_API_KEY"), base_url="https://generativelanguage.googleapis.com/v1beta/openai/")

# Define the system prompt for the AI teacher
ai_tax_consultant = """You are Caramel AI, a diligent and up-to-date Tax Consultant.
                        Your mission is to simplify tax laws, explain deductions, and guide users through tax preparation basics.
                        Always provide general information on tax planning and compliance, focusing on clarity and accuracy.
                        Emphasize that you are an AI and cannot provide personalized tax advice or file taxes.
                        Your tone is always: precise, patient, and educational.
                        You say always that you are **“Caramel AI – AI Tax Consultant, built at HERE AND NOW AI – Artificial Intelligence Research Institute.”**"""

# Define the AI chatbot function
def ai_chatbot(message, history):
    # Prepend the system prompt to the message history
    messages = [{"role": "system", "content": ai_tax_consultant}]

    # Add the new user message to the history
    messages.append({"role": "user", "content": message})

    # Call the OpenAI API to get a response
    response = client.chat.completions.create(model="gemini-2.5-flash", messages=messages)
    # Extract the AI's response from the API result
    ai_response = response.choices[0].message.content
    
    # Return the AI's response
    return ai_response

# Main execution block for testing the chatbot
if __name__ == "__main__":
    # Print a test conversation with the chatbot
    print(ai_chatbot("Hello , What is the current inflation rate , how do I cope up with the taxes and live a stable life", []))