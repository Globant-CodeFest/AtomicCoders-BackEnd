import logging

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)


def chat_with_gpt(message):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": "Bearer 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",
        "Content-Type": "application/json"
    }

    question = "Desde ahora eres un asistente virtual que responde preguntas sobre el FIFA 21 \ " \
               "Vas a identificar los siguientes items de un texto: \ " \
               " - Valor económico del jugador (devolver un valor numérico)" \
               " - Posiciones del jugador buscado (una lista que devuelve uno o más de los siguientes valores: delantero, centrocampista, defensor, arquero)" \
               "El texto está delimitado en \"\"\" \"\"\"." \
               "El formato de respuesta en JSON sin salto de líneas con las claves \"valor\", \"posiciones\"." \
               "Si la información no está presente devolver el valor vacío." \
               " Texto: \"\"\""+message+"\"\"\"\""

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": question},
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()

    messages = response_data["choices"][0]["message"]["content"]
    return messages


@app.route('/api/v1/guru-pront', methods=['GET'])
def get_result_pront():
    client_question_query = request.args.get('client-question')

    app.logger.debug('Client question: %s', client_question_query)

    result = chat_with_gpt(client_question_query)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
