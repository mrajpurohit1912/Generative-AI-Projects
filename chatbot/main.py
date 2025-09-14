import asyncio
import json
from autogen_agentchat.messages import TextMessage

from chatbot.src.core.llms import LLMS
from chatbot.src.core.agents import Agents
from chatbot.src.core.client import get_redis_client

LLM_NAME = "codellama:latest"
AGENT_NAME = "assitantagent"

ollama_llm = LLMS.get_ollama_llm(LLM_NAME)
assitant_agent = Agents.get_assistant_agents(AGENT_NAME,ollama_llm)
redis_client = get_redis_client()

async def main(user_name:str,user_input:str):
    context = await  redis_client.get(user_name)

    if context:
        context = json.loads(context)
        await assitant_agent.load_state(context)
    
    user_message = TextMessage(content=user_input,source=user_name)
    response = await assitant_agent.run(task=user_message)
    print('AI response: ',response.messages[1].content)
    new_context = await assitant_agent.save_state()


    await redis_client.set(user_name,json.dumps(new_context))
    print(f"New context updated")
    return

if __name__ == "__main__":
    user_name = input("Please Enter Your Username: ")
    user_input = input("Ask Anything: ")
    asyncio.run(main(user_name,user_input))