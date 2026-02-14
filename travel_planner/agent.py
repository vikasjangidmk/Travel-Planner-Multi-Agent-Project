import os
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()

# Force set environment variables for LiteLLM
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_BASE_URL"] = "https://openrouter.ai/api/v1"

LLM = "openai/gpt-4o-mini"

root_agent = Agent(
    model=LLM,
    name="travel_planner_main",
    description="A helpful travel planning assistant that helps users plan their trips by providing information and suggestions based on their preferences.",
    instruction="""
            - You are an exclusive travel concierge agent
            - You help users to discover their dream holiday destination and plan their vacation.
            - Use the inspiration_agent to get the best destination, news, places nearby e.g hotels, cafes, etc near attractions and points of interest for the user.
            - You cannot use any tool directly. 
            """,
)