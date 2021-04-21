from flask import Flask, jsonify
from solver.utils import convert_position, invert_position
from solver.models import set_figure

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/api/v1/<chess_figure>/<current_field>", methods=["GET"])
def moves(chess_figure, current_field):
    available_moves_readable = []
    status_code = None
    field = convert_position(current_field)
    if field:
        figure = set_figure(field, chess_figure)
        if figure:
            figure.list_available_moves()
            for move in figure.available_moves:
                available_moves_readable.append(invert_position(move))
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
    if status_code:
        return jsonify(return_data), status_code
    else:
        return jsonify(return_data)


@app.route("/api/v1/<chess_figure>/<current_field>/<dest_field>", methods=["GET"])
def validation(chess_figure, current_field, dest_field):
    is_valid = None
    status_code = None
    current_field_conv = convert_position(current_field)
    dest_field_conv = convert_position(dest_field)
    if current_field_conv and dest_field_conv:
        figure = set_figure(current_field_conv, chess_figure)
        if figure:
            figure.list_available_moves()
            is_valid, error = figure.validate_move(dest_field_conv)
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
    if status_code:
        return jsonify(return_data), status_code
    else:
        return jsonify(return_data)


if __name__ == "__main__":
    app.run(debug=True)
