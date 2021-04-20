X_CONVERT = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

X_INVERTER = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

# From "H5" to (7, 4)
def convert_position(position):
    if len(position) != 2:
        raise Exception("Position in wrong format. Example 'H5'.")
    if position[0] not in X_CONVERT.keys() or position[1] not in X_CONVERT.values():
        raise Exception("Invalid position. Choose from: A to H and 1 to 8.")

    x = X_CONVERT[position[0].lower()]
    y = position[1]
    return (x, y)

# From (7, 4) to "H5"
def invert_position(position):
    x = X_INVERTER[(position[0])].upper()
    y = position[1]
    return f"{x}{y}"