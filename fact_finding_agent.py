#Import all the
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
import os
import sys
from langchain_core.rate_limiters import InMemoryRateLimiter
#Load the api key from env
load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")
model = "gemini-2.0-flash-lite"
#Dictionary containing the data
FACTS = {
    "Capital of France":"Paris",
    "Largest Ocean":"Pacific Ocean",
    "Investor of Telephone":"Alexander Graham Bell",
    "Population of India":"1.4 billion"
}

@tool

def get_fact(query:str) -> str:
    """
    Retrives a fact from a predefined list.The query must be a exact match to one of the available facts

    Available facts are:
    -"Capital of France"
    -"Largest Ocean"
    -"Inventor of Telephone"
    -"Population of India"
    """

    return FACTS.get(query.lower(),"Facts are not found")

def run_data_retrival_agent():
    """
    Creates an agent that can use the get facts tool
    """
    #rate limiter
    rate_limiter = InMemoryRateLimiter(
        requests_per_second=0.1,
         check_every_n_seconds=0.1,
          max_bucket_size=1

    )
    llm = ChatGoogleGenerativeAI(model = model , google_api_key = google_api_key, rate_limiter = rate_limiter)
    tools = [get_fact]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm,tools,prompt)
    agent_executor = AgentExecutor(agent = agent, tools = tools, verbose = True, handle_parsing_errors=True)

    response = []
    print("\n---Query1: Capital of France---")
    response.append(agent_executor.invoke({"input":"What is the Capital of France"}))
    print("\n---Query2: largest ocean---")
    response.append(agent_executor.invoke({"input":"What is the Largest Ocean"}))
    print("\n---Query3: Inventor of telephone---")
    response.append(agent_executor.invoke({"input":"What is the Inventor of Telephone  "}))
    print("\n---Query4: Population of India---")
    response.append(agent_executor.invoke({"input":"What is the Population of India"}))

    print("\n\n---Final Answer---")
    for i,response in enumerate(response,1):
        print(f"Response {i}: {response['output']}")


if __name__ =="__main__":
    run_data_retrival_agent()    
