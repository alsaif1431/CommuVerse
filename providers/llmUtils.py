from langchain_openai import AzureChatOpenAI
import os
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults


def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=os.getenv('AZURE_OPENAI_ENDPOINT'),
        azure_deployment=os.getenv('AZURE_OPENAI_DEPLOYMENT_NAME'),
        api_key=os.getenv('AZURE_OPENAI_API_KEY'),
        api_version=os.getenv('AZURE_OPENAI_API_VERSION')
    )


def get_chat_memory(key="default_key"):
    msgs = StreamlitChatMessageHistory(key=key)
    return ConversationBufferMemory(chat_memory=msgs, return_messages=True)



def create_agent(system_message, llm, memory):
    agent_kwargs = {
        "system_message": system_message,
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="history")]
    }
    return initialize_agent(
        tools=[TavilySearchResults(max_results=1)],  # Add tools as needed
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory
    )
