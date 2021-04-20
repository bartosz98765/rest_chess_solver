from chess import King

def main(field, name, dest_field):
    figure = None
    if name == "king":
        figure = King(field, name)
        print(f'{figure.name} z {field} na {dest_field}' )
        print(f'King id: {figure.figure_id}')

    if figure:
        available_moves = figure.list_available_moves()
        print(f'Możliwe ruchy: {available_moves}')

    if figure:
        is_available = figure.validate_move(dest_field)
        print(f'Czy ruch jest możliwy: {is_available}')
        print('')

if __name__ == '__main__':

    main((1,1), 'king', list((2, 2)))
    main((5,5), 'king', (3,3))
    main((-1,0), 'king', (1,1))