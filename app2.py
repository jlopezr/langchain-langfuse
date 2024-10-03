#!/usr/bin/env python
import os
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langserve import add_routes
from langfuse.callback import CallbackHandler
from langchain_core.runnables.config import RunnableConfig

# 1. Create prompt template
system_template = "Translate the following into {language}, please do not add extra comments or notes only the translation:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# 2. Create model
openai_api_key = os.getenv('OPENAI_API_KEY')
if openai_api_key is not None:
    model = ChatOpenAI(api_key=openai_api_key)
else:
    model = ChatOllama(
        model = "llama3",    
        base_url = "http://localhost:11434"
    )

# 3. Create parser
parser = StrOutputParser()

# 4. Create chain
chain = prompt_template | model | parser

# 6. Create langfuse handler
langfuse_handler = CallbackHandler(
  secret_key="sk-lf-f6ce6953-e0ab-4c83-b63e-44c9ed5f5e8e",
  public_key="pk-lf-c6091478-c5fb-4536-ae22-1639d372cff5",
  host="http://localhost:3000",  
)
langfuse_handler.auth_check() # Tests the SDK connection with the server
config = RunnableConfig(callbacks=[langfuse_handler])
chain_with_langfuse = chain.with_config(config)

# 4. App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# 5. Adding chain route
add_routes(
    app,
    chain_with_langfuse,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)