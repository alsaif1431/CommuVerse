from langchain_openai import AzureChatOpenAI
import os   
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.prompts import MessagesPlaceholder
from langchain.agents import initialize_agent, AgentType
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv(override=True)

def get_llm():
    return AzureChatOpenAI(
        azure_endpoint=st.secrets.get("AZURE_OPENAI_ENDPOINT"),
        azure_deployment=st.secrets.get("AZURE_OPENAI_DEPLOYMENT_NAME"),
        api_key=st.secrets.get("AZURE_OPENAI_API_KEY"),
        api_version=st.secrets.get("AZURE_OPENAI_API_VERSION"),
    )
    # return ChatAnthropic(model='claude-3-opus-20240229')

def get_chat_memory():
    if "chat_memory" not in st.session_state:
        st.session_state.chat_memory = ConversationBufferMemory(return_messages=True)
    return st.session_state.chat_memory

def create_agent(system_message, llm, memory):
    agent_kwargs = {
        "system_message": system_message,
        "extra_prompt_messages": [MessagesPlaceholder(variable_name="history")]
    }
    return initialize_agent(
        tools=[TavilySearchResults(max_results=1)], 
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        agent_kwargs=agent_kwargs,
        memory=memory
    )