from flask import Flask, jsonify
from models import King

app = Flask(__name__)

CHESS_FIGURES = ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn')
X_CONVERT = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
X_INVERTER = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
Y_VALUES = '12345678'

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
        rv['error'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


# From "H5" to (7, 4)
def convert_position(position):
    if len(position) != 2 or position[0] not in X_CONVERT.keys() or position[1] not in Y_VALUES:
        return None

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
    available_moves_readable = []
    status_code = 200


    # if chess_figure not in CHESS_FIGURES:
    #     status_code = 404
    #     error = "Figure does not exit."
        # raise InvalidUsage(f"Invalid figure. Choose from: {', '.join(CHESS_FIGURES)}", status_code=404)
    field = convert_position(current_field)
    if field:
        if chess_figure == "king":
            figure = King(field, chess_figure)
            figure.list_available_moves()
            for el in figure.available_moves:
                available_moves_readable.append(invert_position(el))
            available_moves_readable.sort()
        else:
            status_code = 404
            error = "Figure does not exit."
    else:
        status_code = 409
        error = "Field does not exit."

    # if figure:
    #     figure.list_available_moves()
    #     for el in figure.available_moves:
    #         available_moves_readable.append(invert_position(el))
    #     available_moves_readable.sort()

    return_data = {
        "availableMoves": available_moves_readable,
        "error": error,
        "figure": chess_figure,
        "currentField": current_field.upper(),
    }
    return jsonify(return_data), status_code


@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def validation(chess_figure, current_field, dest_field):
    figure = None
    is_valid = None
    if chess_figure not in CHESS_FIGURES:
        raise InvalidUsage(f"Invalid figure. Choose from: {', '.join(CHESS_FIGURES)}", status_code=404)


    if chess_figure == "king":
        figure = King(convert_position(current_field), chess_figure)
    if figure:
        figure.list_available_moves()
        is_valid = figure.validate_move(convert_position(dest_field))


    return_data = {
        "move": is_valid,
        "figure": figure.name,
        "error": figure.error,
        "currentField": current_field.upper(),
        "destField": dest_field.upper(),
    }
    return jsonify(return_data)


if __name__ == '__main__':
    app.run()
