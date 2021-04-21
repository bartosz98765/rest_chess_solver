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

    # @abstractmethod
    def validate_move(self, dest_field):
        if dest_field in self.available_moves:
            is_valid = "valid"
            error = None
        else:
            is_valid = "invalid"
            error = "Current move is not permitted"
        return is_valid, error


class King(Figure):
    KING_MOVES = ((1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1))

    def list_available_moves(self):
        for el in self.KING_MOVES:
            if 0 <= self.field[0] + el[0] < 8 and 0 <= self.field[1] + el[1] < 8:
                self.available_moves.append(tuple(a + b for a, b in zip(self.field, el)))

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error


class Rook(Figure):

    def list_available_moves(self):
        self.available_moves = [(x, self.field[1]) for x in range(0, 8)]
        self.available_moves.remove(self.field)
        self.available_moves += [(self.field[0], y) for y in range(0, 8)]
        self.available_moves.remove(self.field)

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error


class Bishop(Figure):

    def list_available_moves(self):
        # vertical moves
        x_offset = self.field[1] - self.field[0]
        y_offset = sum(self.field)
        rightup_moves = [(x - x_offset, x) for x in range(0, 8) if 0 <= x - x_offset < 8]
        rightup_moves.remove(self.field)
        leftdown_moves = [(x, y_offset - x) for x in range(0, 8) if 0 <= y_offset - x < 8]
        leftdown_moves.remove(self.field)
        self.available_moves = rightup_moves + leftdown_moves

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error


class Queen(Figure):

    def list_available_moves(self):
        # vertical moves
        x_offset = self.field[1] - self.field[0]
        y_offset = sum(self.field)
        rightup_moves = [(x - x_offset, x) for x in range(0, 8) if 0 <= x - x_offset < 8]
        rightup_moves.remove(self.field)
        leftdown_moves = [(x, y_offset - x) for x in range(0, 8) if 0 <= y_offset - x < 8]
        leftdown_moves.remove(self.field)
        self.available_moves = rightup_moves + leftdown_moves
        # horizontal moves
        self.available_moves += [(x, self.field[1]) for x in range(0, 8)]
        self.available_moves.remove(self.field)
        self.available_moves += [(self.field[0], y) for y in range(0, 8)]
        self.available_moves.remove(self.field)

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error


class Knight(Figure):
    MOVE_OFFSETS = [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

    def list_available_moves(self):
        for el in self.MOVE_OFFSETS:
            if 0 <= self.field[0] + el[0] < 8 and 0 <= self.field[1] + el[1] < 8:
                self.available_moves.append(tuple(a + b for a, b in zip(self.field, el)))

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error


class Pawn(Figure):
    # CAUTIONS: moves set only for WHITES!
    # for BLACK have to be set "-" at y-position
    MOVE_OFFSETS = [(0, 1)]
    START_MOVE_OFFSETS = [(0, 1), (0, 2)]

    def list_available_moves(self):
        # CAUTION: todo: error message for first row
        if self.field[1] < 1:
            return
        elif self.field[1] == 1:
            moves = self.START_MOVE_OFFSETS
        else:
            moves = self.MOVE_OFFSETS

        for el in moves:
            if 0 <= self.field[0] + el[0] < 8 and 0 <= self.field[1] + el[1] < 8:
                self.available_moves.append(tuple(a + b for a, b in zip(self.field, el)))

    # def validate_move(self, dest_field):
    #     if dest_field in self.available_moves:
    #         is_valid = "valid"
    #         error = None
    #     else:
    #         is_valid = "invalid"
    #         error = "Current move is not permitted"
    #     return is_valid, error
