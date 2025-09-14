from autogen_agentchat.agents import AssistantAgent
from chatbot.src.core.llms import LLMS



class Agents:
    def get_assistant_agents(agent_name:str,llm):
        my_agent = AssistantAgent(agent_name,llm)
        return my_agent

