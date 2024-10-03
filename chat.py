import os

openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    from config_ollama import model
else:    
    from config_openai import model

def get_response(user_input):    
    # Generate a response from the model
    response = model.invoke(user_input)
    return response