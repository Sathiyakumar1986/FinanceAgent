import os

from dotenv import load_dotenv
from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
import phi
from phi.playground import Playground,serve_playground_app

load_dotenv()
# Setting API key
phi.api_key = os.getenv('PHI_API_KEY')
print("PHI_API_KEY:", os.getenv("PHI_API_KEY"))
# Web search agent
# Creating the Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Creating the Financial Agent
financial_agent = Agent(
    name="Financial AI Agent",
    role="Analyze stock market data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)


app = Playground(agents=[web_search_agent, financial_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
