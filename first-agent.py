import asyncio
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv()

    client = MCPClient.from_config_file(
        os.path.join("mcp_setting.json")
    )

    # Create LLM
    llm = ChatOpenAI(model="gpt-4.1-mini")

    # Create agent with the client
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=30,
        disallowed_tools=["Bash", "dispatch_agent"]
    )

    print("対話型MCPクライアントです。終了するには 'exit' と入力してください。")
    while True:
        user_input = input("あなた: ")
        if user_input.strip().lower() == "exit":
            print("終了します。")
            break

        result = await agent.run(user_input)
        print(f"エージェント: {result}\n")

if __name__ == "__main__":
    asyncio.run(main())