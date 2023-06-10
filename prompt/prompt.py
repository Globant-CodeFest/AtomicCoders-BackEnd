import requests

# Define los parámetros de la solicitud
url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
}

# Envía la solicitud POST a la API
response = requests.post(url, headers=headers, json=data)
response_data = response.json()

# Procesa la respuesta
for message in response_data["choices"][0]["message"]["content"]:
    role = message["role"]
    content = message["content"]
    print(f"{role}: {content}")