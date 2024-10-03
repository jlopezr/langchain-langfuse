from langchain_ollama.llms import OllamaLLM

# setup Ollama server URL
ollama_url = "http://localhost:11434"

model = OllamaLLM(model="llama3", base_url=ollama_url)

# Specify the symbols to be exported
__all__ = ['model']