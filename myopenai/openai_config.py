from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")


def get_embeddings():
    return OpenAIEmbeddings(model='text-embedding-ada-002', openai_api_key=openai_api_key)


def get_model():
    return OpenAI(model_name='text-ada-001', openai_api_key=openai_api_key)


def get_chat_model():
    return ChatOpenAI(openai_api_key=openai_api_key)

