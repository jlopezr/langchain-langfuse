import langserve
import sys
from langserve import RemoteRunnable

def test_chat(query=None):    
    try:
        client = RemoteRunnable("http://localhost:8000/chain/")
        response = client.invoke({"language": "italian", "text": query})
        print("Response from server:", response)

    except langserve.LangServeError as e:
        print("Failed to get response. Error:", str(e))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = "What's the capital of Catalonia?"
    test_chat(query)