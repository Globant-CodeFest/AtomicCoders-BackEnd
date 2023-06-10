import logging

from flask import Flask, jsonify, request

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

def process_question(clientQuestionQuery):

    return [{
        'sofifa_id': 1,
        'short_name': 'Leonel Messi',
        'age': 32,
        'nationality_name': 'Argentina',
        'value_eur': 100000000,
        'wage_eur': 1000000,
        'player_positions': ['RW', 'ST', 'CF'],
        'club_name': 'Barcelona',
        'player_face_url': 'https://cdn.sofifa.org/players/4/19/158023.png',
        'pace': 87.1,
        'passing': 90.0,
        'shooting': 95.0,
        'dribbling': 96.0,
        'defending': 32.0,
        'physic': 61.0
    }]

@app.route('/api/v1/guru-pront', methods=['GET'])
def get_result_pront():

    clientQuestionQuery = request.args.get('client-question')

    app.logger.debug('Client question: %s', clientQuestionQuery)

    result = process_question(clientQuestionQuery)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
