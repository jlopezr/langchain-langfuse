import os

# Initialize model
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    from config_ollama import model
else:    
    from config_openai import model

 # Initialize Langfuse handler
from langfuse.callback import CallbackHandler
langfuse_handler = CallbackHandler(
  secret_key="sk-lf-f6ce6953-e0ab-4c83-b63e-44c9ed5f5e8e",
  public_key="pk-lf-c6091478-c5fb-4536-ae22-1639d372cff5",
  host="http://localhost:3000"
)

def get_response(user_input):    
    # Generate a response from the model
    response = model.invoke(user_input, config={"callbacks": [langfuse_handler]})
    return response