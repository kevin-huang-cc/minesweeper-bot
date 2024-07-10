from minesweeper import core


def main():
    board = core.Board(rows=10, cols=10, mines=30)

    tiles = board.tile_open(5, 5)
    for tile in tiles:
        print(f"tile={tile.type}, ({tile.i}, {tile.j})")
    print(board.is_game_over)
    print(board.is_game_finished)
    print(board)
    print(board.solution)


if __name__ == "__main__":
    main()