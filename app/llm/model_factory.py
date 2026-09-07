from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

def get_model() -> BaseChatModel:
    return ChatOpenAI(
        model="gpt-5-nano",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )