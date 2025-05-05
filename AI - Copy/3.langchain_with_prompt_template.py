from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
import os

# Set up API with error handling
os.environ["OPENAI_API_KEY"] = "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"


sys_msg = "You are {subject} teacher"
human_msg = "Tell me about the {concept}"

prompt_template = ChatPromptTemplate.from_messages([("system",sys_msg),("human",human_msg)])

prompt = prompt_template.format_messages(subject="Chemistry", concept="Periodic Table")

