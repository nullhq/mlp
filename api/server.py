from flask import Flask, request, jsonify
from flask_cors import CORS
from module import repondre_iris

server = Flask(__name__)
CORS(server)

@server.route('/api', methods=['POST'])
def get_iris_specie():
    # get sepal length, sepal width, petal length, petal width from request
    iris_size_data = request.get_json()

    if not iris_size_data:
        return jsonify({'error': 'Aucune information n\'a été envoyée.'}), 400
    
    if not all(key in iris_size_data for key in ('spH', 'spW', 'ptH', 'ptW')):
        return jsonify({'error': 'Les informations envoyées sont incorrectes.'}), 400
    
    try:
        longeur_sepale = float(iris_size_data['spH'])
        largeur_sepale = float(iris_size_data['spW'])
        longeur_petale = float(iris_size_data['ptH'])
        largeur_petale = float(iris_size_data['ptW'])
    except ValueError:
        return jsonify({'error': 'Les informations envoyées sont incorrectes ou ne peuvent pas etre formatées.'}), 400
    
    features = [longeur_sepale, largeur_sepale, longeur_petale, largeur_petale]
    result = repondre_iris(features)
    
    return jsonify(result), 201


if __name__ == '__main__':
    server.run(debug=True)


