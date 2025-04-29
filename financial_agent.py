from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

# Creating the Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions="Always include sources",
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
    instructions="Use tables to display the data",
    show_tool_calls=True,
    markdown=True
)

# Combining Agents into a Multi-Model Agent

multi_agent=Agent(
    team=[web_search_agent,financial_agent],
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions=["Always include sources. Use tables to display data."],
    show_tool_calls=True,
    markdown=True,
)

# Running the Multi-Agent for a query
response = multi_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA")
print(response)
