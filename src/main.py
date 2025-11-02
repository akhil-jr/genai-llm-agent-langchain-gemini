"""
Fully Working LangChain Agent with Gemini
"""

import os
import asyncio
from datetime import datetime, date
from typing import Any, Dict, List
#from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from dotenv import load_dotenv
from langchain_core.callbacks import CallbackManager
from .callback_handler import APICallLogger
from .tools import order_details, customer_details, approve_or_reject

load_dotenv()


def create_final_agent():
    """Create the agent with Gemini"""

    callback_manager = CallbackManager(handlers=[APICallLogger()])
    
    # Check for API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is required")
    
    # LLM Configuration
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=api_key,
        temperature=0.1,
        convert_system_message_to_human=True,
        callbacks=callback_manager
    )
    
    # System Prompt
    system_prompt = f"""You are an intelligent return decision agent. Use available tools to approve or reject product return requests.

Current date: {date.today()}

Follow this systematic approach. Use availabe tools to find required details:

1. Check if request is within return window
2. Check if customer trust score > 5
3. Use `approve_or_reject` tool for final decision

Decision Rules:
- APPROVE: Within return window AND trust score > 5
- REJECT: Outside return window OR trust score ≤ 5

IMPORTANT: You MUST use the tools - never make decisions without calling them first. Think step by step and use the tools systematically."""
    
    # Tools
    tools = [order_details, customer_details, approve_or_reject]
    
    # Create agent
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=system_prompt
    )
    return agent


# ==================== EXECUTION ====================
async def run_agent_workflow(user_input: str):
    """Run the actual agent workflow"""
    
    print("LANGCHAIN AGENT")
    print(f"Input: {user_input}")
    
    # Create the agent
    agent = create_final_agent()
    
    # Execute the agent
    print("\nAGENT EXECUTING...")
    result = await agent.ainvoke({"messages": [("human", user_input)]})
    
    print("\n" + "="*50)
    print("FINAL RESULT:")
    print("="*50)
    print(f"Final Output: {result}")
    
    return result


# ==================== MAIN ====================
async def main():
    """Main execution"""
    
    # Use default input for testing
    user_input = "i want to return order 123"
    
    # Run the agent
    await run_agent_workflow(user_input)


if __name__ == "__main__":
    asyncio.run(main())
    #await main()