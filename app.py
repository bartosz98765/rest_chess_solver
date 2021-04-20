from flask import Flask, request, render_template, jsonify
from chess import King

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
        available_moves = figure.list_available_moves()

    # available_moves = ["B3","B3","A3","C1","C3","B2"]
    # current_field = "B2"
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
    error = None
    is_valid = None
    if current_field == "b2":
        current_field = [1, 1]
    available_moves = []

    if chess_figure == "king":
        figure = King(current_field, chess_figure)

    if figure:
        available_moves = figure.list_available_moves()
        is_available = figure.validate_move(dest_field)

    current_field = "B2"
    dest_field = "C2"

    return_data = {
        "move": is_valid,
        "figure": figure.name,
        "error": error,
        "currentField": current_field,
        "destField": dest_field
    }

    return jsonify(return_data)


if __name__ == '__main__':
    app.run()
