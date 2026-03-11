import requests
def ask_llm(text):
    r=requests.post(
        "http://localhost:3000/chat",
        json={"text":text}
    )
    return r.json()["response"]