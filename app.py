import flask
from flask import request, jsonify

import fasttext
import pandas as pd

from utils import *

app = flask.Flask(__name__)

df = pd.read_csv("data/entity_types.csv")
model = fasttext.load_model('data/wiki.en.bin')

vocab_list = df['preprocessed_label'].values.tolist()
vocab_vectors = {w: model.get_sentence_vector(w) for w in vocab_list}


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Machines Reading Maps - Entity Recommendation API</h1>
<a href="https://github.com/machines-reading-maps/mrm-entity-api-demo">link to document</a>'''


@app.route('/entities/all', methods=['GET'])
def api_all():
    return jsonify({"all_entities": vocab_list})


@app.route('/entities', methods=['GET'])
def api_id():
    if 'input' in request.args:
        user_input = request.args['input']
    else:
        return "Error: No input field provided. Please specify user input."

    comp_dict = compare_word(user_input, model, vocab_vectors)
    sorted_dict = dict(sorted(comp_dict.items(), key=lambda item: item[1], reverse=True))
    entities = find_elbow_point(sorted_dict)

    candidates = []

    for i, entity in enumerate(entities):
        result_dict = {}
        result_dict['rank'] = i
        result_dict['entity'] = entity
        result_dict['uri'] = df.loc[df['preprocessed_label'] == entity, 'id'].values[0]
        candidates.append(result_dict)

    return jsonify({"input": user_input, "candidates": candidates})


if __name__ == '__main__':
    app.run(debug=True, port=8000)
