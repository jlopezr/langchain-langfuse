from langchain import OpenAI
import os

# Ensure you have set your OpenAI API key as an environment variable
openai_api_key = os.getenv('OPENAI_API_KEY')

# Initialize the OpenAI model
model = OpenAI(api_key=openai_api_key)

# Specify the symbols to be exported
__all__ = ['model']