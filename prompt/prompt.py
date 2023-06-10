import requests

message = "tengo 2000000 EUR quiero al delantero mas veloz para mi equipo?"
def chat_with_gpt(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    assistant_response = response_data["choices"][0]["message"]["content"]
    return assistant_response

# Ejemplo de uso
api_key = "YOUR_API_KEY"
user_input = input("User: ")

response = chat_with_gpt(user_input)
print("ChatGPT:", response)
