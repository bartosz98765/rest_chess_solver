X_CONVERT = {
    "a": "0",
    "b": "1",
    "c": "2",
    "d": "3",
    "e": "4",
    "f": "5",
    "g": "6",
    "h": "7",
}
X_INVERTER = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}
Y_VALUES = "12345678"


# From "H5" -> (7, 4)
def convert_position(position):
    if (
        len(position) == 2
        and position[0] in X_CONVERT.keys()
        and position[1] in Y_VALUES
    ):
        x = int(X_CONVERT[position[0].lower()])
        y = int(position[1]) - 1
        return x, y


# From (7, 4) -> "H5"
def invert_position(position):
    x = X_INVERTER[(position[0])].upper()
    y = position[1] + 1
    return f"{x}{y}"
