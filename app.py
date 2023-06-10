import logging
import json

from flask import Flask, jsonify, request
import data_extraction

from prompt import prompt

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route('/api/v1/guru-pront', methods=['GET'])
def get_result_pront():

    client_question_query = request.args.get('client-question')

    app.logger.info('GET ==> /api/v1/guru-pront?client-question=%s ==> Pending...', client_question_query)

    result = prompt.chat_with_gpt(client_question_query)

    app.logger.debug('Prompt Result: %s', result)

    result_to_dictionary = json.loads(result)

    dictionary_result = data_extraction.player_request(result_to_dictionary)

    app.logger.info('GET ==> /api/v1/guru-pront?client-question=%s ==> Response %s', client_question_query, result)

    return jsonify(dictionary_result)


if __name__ == '__main__':
    app.run()
