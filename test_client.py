import requests

def test_chat():
    url = "http://127.0.0.1:5000/chat"
    payload = {"message": "What's the capital of Catalonia?"}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        print("Response from server:", response.json())
    else:
        print("Failed to get response. Status code:", response.status_code)

if __name__ == "__main__":
    test_chat()