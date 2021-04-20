from flask import Flask, jsonify
from models import King

app = Flask(__name__)

CHESS_FIGURES = ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn')
X_CONVERT = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
X_INVERTER = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# From "H5" to (7, 4)
def convert_position(position):
    if len(position) != 2:
        raise InvalidUsage("Field in wrong format. Example 'H5'.", status_code=409)
    if position[0] not in X_CONVERT.keys() or position[1] not in X_CONVERT.values():
        raise InvalidUsage("Invalid field value. Choose from: A to H and 1 to 8.", status_code=409)

    x = int(X_CONVERT[position[0].lower()])
    y = int(position[1])
    return (x, y)


# From (7, 4) to "H5"
def invert_position(position):
    x = X_INVERTER[(position[0])].upper()
    y = position[1]
    return f"{x}{y}"


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def moves(chess_figure, current_field):
    figure = None
    error = None
    available_moves = []

    if chess_figure not in CHESS_FIGURES:
        raise InvalidUsage(f"Invalid figure. Choose from: {' ,'.join(CHESS_FIGURES)}", status_code=404)

    field = convert_position(current_field)
    if chess_figure == "king":
        figure = King(field, chess_figure)
    if figure:
        figure.list_available_moves()
    for el in figure.available_moves:
        available_moves.append(invert_position(el))
    available_moves.sort()

    return_data = {
        "availableMoves": available_moves,
        "error": error,
        "figure": figure.name,
        "currentField": current_field.upper()
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
