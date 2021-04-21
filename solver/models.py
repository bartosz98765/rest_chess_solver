from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, field, name):
        self._field = field if self._field_check(field) else None
        self.name = name
        self.available_moves = []

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
    KING_MOVES = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))

    def list_available_moves(self):
        for el in King.KING_MOVES:
            if 0 <= self.field[0] + el[0] < 8 and 0 <= self.field[1] + el[1] <= 8:
                self.available_moves.append([a + b for a, b in zip(self.field, el)])

    def validate_move(self, dest_field):
        if list(dest_field) in self.available_moves:
            is_valid = "valid"
            error = None
        else:
            is_valid = "invalid"
            error = "Current move is not permitted"
        return is_valid, error
