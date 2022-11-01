from typing import List
from queue import Queue

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]


def get_valid_neighbour(board, x, y, old='.') -> List[List[int]]:
    """Returns the neighbours of the given point that can be filled
    Args:
        board (List[str]) given board to check
        x (int): Index on the vertical axis of the board
        y (int): Index on the horizontal axis of the board
        old (str): value to be replaced (or can be replaced)
    """
    return [v for v in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] if 0 <= v[0] < len(board) and 0 <= v[1] < len(board[v[0]]) and board[v[0]][v[1]] == old]


def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values
    through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str]) given board to fill
        old (str): Value to be replaced
        new (str): Value for replacing
        x (int): index on the vertical axis
        y (int): index on the horizontal axis
    Returns:
        List[str]: Modified board
    """
    new_board = board.copy()
    q = Queue()
    if input_board[x][y] == old:
        q.put((x, y))
        while not q.empty():
            x, y = q.get()
            board_str_list = list(new_board[x])
            board_str_list[y] = new
            new_board[x] = ''.join(board_str_list)
            valid_neighbours = get_valid_neighbour(new_board, x, y)
            for nei in valid_neighbours:
                q.put(nei)
    return new_board

    
if __name__ == "__main__":

    ans = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
    for a in ans:
        print(a)