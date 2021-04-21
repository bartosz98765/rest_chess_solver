from flask import Flask, jsonify
from solver.models import King, Rook, Bishop, Queen, Knight, Pawn

app = Flask(__name__)

CHESS_FIGURES = ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn')
X_CONVERT = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
X_INVERTER = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}
Y_VALUES = '12345678'


# From "H5" to (7, 4)
def convert_position(position):
    if len(position) == 2 and position[0] in X_CONVERT.keys() and position[1] in Y_VALUES:
        x = int(X_CONVERT[position[0].lower()])
        y = int(position[1])-1
        return x, y


# From (7, 4) to "H5"
def invert_position(position):
    x = X_INVERTER[(position[0])].upper()
    y = position[1]+1
    return f"{x}{y}"


def set_figure(field, name):
    figure = None
    if name == 'king':
        figure = King(field, name)
    if name == 'rook':
        figure = Rook(field, name)
    if name == 'bishop':
        figure = Bishop(field, name)
    if name == 'queen':
        figure = Queen(field, name)
    if name == 'knight':
        figure = Knight(field, name)
    if name == 'pawn':
        figure = Pawn(field, name)
    return figure


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/v1/<chess_figure>/<current_field>', methods=['GET'])
def moves(chess_figure, current_field):
    available_moves_readable = []
    status_code = 200
    field = convert_position(current_field)
    if field:
        figure = set_figure(field, chess_figure)
        if figure:
            figure.list_available_moves()
            for el in figure.available_moves:
                available_moves_readable.append(invert_position(el))
            available_moves_readable.sort()
            error = None
        else:
            status_code = 404
            error = "Figure does not exist."
    else:
        status_code = 409
        error = f"Field does not exist."

    return_data = {
        "availableMoves": available_moves_readable,
        "error": error,
        "figure": chess_figure,
        "currentField": current_field.upper(),
    }
    return jsonify(return_data), status_code


@app.route('/api/v1/<chess_figure>/<current_field>/<dest_field>', methods=['GET'])
def validation(chess_figure, current_field, dest_field):
    is_valid = None
    status_code = 200
    current_field_list = convert_position(current_field)
    dest_field_list = convert_position(dest_field)
    if current_field_list and dest_field_list:
        figure = set_figure(current_field_list, chess_figure)
        if figure:
            figure.list_available_moves()
            is_valid, error = figure.validate_move(dest_field_list)
        else:
            status_code = 404
            error = "Figure does not exist."
    else:
        status_code = 409
        error = "Field does not exist."

    return_data = {
        "move": is_valid,
        "figure": chess_figure,
        "error": error,
        "currentField": current_field.upper(),
        "destField": dest_field.upper(),
    }
    return jsonify(return_data), status_code


if __name__ == '__main__':
    app.run(debug=True)
