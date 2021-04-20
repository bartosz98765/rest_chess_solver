from abc import ABC, abstractmethod

# STARTING_BOARD = [["W", "W", "W", "W", "W", "W", "W", "W"],
#                   ["W", "W", "W", "W", "W", "W", "W", "W"],
#                   ["", "", "", "", "", "", "", ""],
#                   ["", "", "", "", "", "", "", ""],
#                   ["", "", "", "", "", "", "", ""],
#                   ["", "", "", "", "", "", "", ""],
#                   ["B", "B", "B", "B", "B", "B", "B", "B"],
#                   ["B", "B", "B", "B", "B", "B", "B", "B"]]


class Figure(ABC):
    figure_id = 1

    def __init__(self, field, name):
        self._field = field if self._field_check(field) else None
        self.name = name
        self.available_moves = []
        self.figure_id = Figure.figure_id
        Figure.figure_id += 1

    @staticmethod
    def _field_check(field):
        return 0 <= field[0] < 8 and 0 <= field[1] <= 8

    @property
    def field(self):
        return self._field

    @field.setter
    def field(self, field):
        self._field = field if self._field_check(field) else None

    @abstractmethod
    def list_available_moves(self):
        pass

    @abstractmethod
    def validate_move(self, dest_field):
        pass


class King(Figure):
    KING_MOVES = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    def list_available_moves(self):
        if self.field:
            for el in King.KING_MOVES:
                if 0 <= self.field[0] + el[0] < 8 and 0 <= self.field[1] + el[1] <= 8:
                    self.available_moves.append([a + b for a, b in zip(self.field, el)])
        return self.available_moves

    def validate_move(self, dest_field):
        if dest_field in self.available_moves:
            return True
        else:
            return False
