import logging
import json

from flask import Flask, jsonify, request
from flask_cors import CORS
import data_extraction

from prompt import prompt

app = Flask(__name__)

CORS(app)


logging.basicConfig(level=logging.DEBUG)


@app.route('/api/v1/guru-pront', methods=['GET'])
def get_result_pront():

    client_question_query = request.args.get('client-question')

    app.logger.info('GET ==> /api/v1/guru-pront?client-question=%s ==> Pending...', client_question_query)

    dictionary_result = []

    try:
        result = prompt.chat_with_gpt(client_question_query)

        app.logger.debug('Prompt Result: %s', result)

        result_to_dictionary = json.loads(result)

        dictionary_result = data_extraction.player_request(result_to_dictionary)

    except Exception:
        app.logger.error('Promp fails')

    app.logger.info('GET ==> /api/v1/guru-pront ==> 200')

    return jsonify(dictionary_result)


if __name__ == '__main__':
    app.run()
