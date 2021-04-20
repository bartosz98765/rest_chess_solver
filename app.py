from flask import Flask, request, render_template, jsonify
from models import King

app = Flask(__name__)


# [GET] `/api/v1/{chess-figure}/{current-field}` (wyświetla listę możliwych ruchów)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def moves(chess_figure, current_field):
    figure = None
    error = None
    if current_field == "b2":
        current_field = [1, 1]
    available_moves = []

    if chess_figure == "king":
        figure = King(current_field, chess_figure)

    if figure:
        figure.list_available_moves()
        available_moves = figure.available_moves

    return_data = {
        "availableMoves": available_moves,
        "error": error,
        "figure": figure.name,
        "currentField": current_field
    }

    return jsonify(return_data)


@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def validation(chess_figure, current_field, dest_field):
    figure = None
    is_valid = None
    if current_field == "b2":
        current_field = [1, 1]
    if dest_field == "d4":
        dest_field = [3, 3]
    available_moves = []

    if chess_figure == "king":
        figure = King(current_field, chess_figure)

    if figure:
        figure.list_available_moves()
        is_valid = figure.validate_move(dest_field)

    current_field = "B2"
    dest_field = "D4"

    return_data = {
        "move": is_valid,
        "figure": figure.name,
        "error": figure.error,
        "currentField": current_field,
        "destField": dest_field
    }

    return jsonify(return_data)


if __name__ == '__main__':
    app.run()
