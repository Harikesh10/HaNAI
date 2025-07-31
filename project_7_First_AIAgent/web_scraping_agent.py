from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor , create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
import os
import ast #abstract syntax tree

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash"

@tool 
def web_scrape_tool(urls:str) -> str:
    """
    This is a scraping procedure from a list of urls
    The input should be a string represntation of a python list of url's
    (e.g., "['https://www.sathyabama.ac.in','https://hereandnowai.com']")
    """
    try:
        url_list = ast.literal_eval(urls)
        if not isinstance(url_list , list) or not all(isinstance(url,str) for url in url_list):
            return "Invalid input format. Please provide a list of URLs as a string (e.g., \"['https://www.sathyabama.ac.in']\")"
    except(ValueError,SyntaxError):
        return "Invalid input format. Please provide a list of URLs as a string (e.g., \"['https://www.sathyabama.ac.in']\")"
    
    combined_content = []
    for url in url_list:
        try:
            loader = WebBaseLoader(
                [url],requests_kwargs={"headers":{"User-Agent":"Jarvis"}}

            )
            documents = loader.load()
            for doc in documents:
                combined_content.append(doc.page_content)
        except Exception as e:
            combined_content.append(f"Could not scrape {url} Error {e}")
    return "\n\n".join (combined_content)

def run_web_scraping_agent():
    """
    Creates and runs an agent that can use the web scrape tool
    """

    llm = ChatGoogleGenerativeAI(model = model , google_api_key= google_api_key)
    tools =[web_scrape_tool]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm,tools,prompt)
    agent_executor = AgentExecutor(agent=agent, tools = tools, verbose= True,handle_parsing_errors=True)
    print("\n---Query1:Get content from home page ---")
    question_home_page ="What is the story of here and now ai? The url is https://hereandnowai.com/ "
    response_home_page = agent_executor.invoke({"input":question_home_page})
    print(f"Agent response: {response_home_page['output']}")

if __name__ == "__main__":
    run_web_scraping_agent()



