import requests
import json

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

    messages = response_data["choices"][0]["message"]["content"]
    return messages

# Ejemplo de uso
api_key = "YOUR_API_KEY"

mensaje = "Dame a los mejores jugadores del mundo en json"

response = chat_with_gpt(mensaje)
response_json = json.dumps(response)  # Convertir la lista de mensajes a JSON
print(response_json)