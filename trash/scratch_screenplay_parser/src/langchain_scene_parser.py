import os
from dotenv import load_dotenv
from system_prompt import screenplay_parser_bot
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers.structured import StructuredOutputParser
from response_template import output_parser_schema
from langchain.prompts import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()

# Initialize the chat model
chat_model = ChatOpenAI(model_name='gpt-3.5-turbo-16k', api_key=os.environ.get("OPENAI_API_KEY"))

# Initialize the chat template outside the function
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content=screenplay_parser_bot),
    HumanMessagePromptTemplate.from_template("{text}"),
])

# Initialize the chat chain outside the function
chat_chain = LLMChain(llm=chat_model, prompt=chat_template, output_parser=output_parser_schema)

def run_chat_chain(text_query):
    extracted_data = chat_chain.run(text_query)
    return extracted_data

# Example usage
# Assuming text_query is defined earlier
# result1 = run_chat_chain(text_query="Query 1")
# result2 = run_chat_chain(text_query="Query 2")

