def create_player(player_name, player_color):
    return {"name": player_name, "color": player_color}


def create_connect_four_game(p1_name, p1_color, p2_name, p2_color, rows=6, cols=7):
    game_board = [[-1 for _ in range(cols)] for _ in range(rows)]
    players = [
        create_player(p1_name, p1_color),
        create_player(p2_name, p2_color),
    ]
    return {"game_board": game_board, "players": players, "turn": 0}


def drop_piece(game_state, column):
    game_board = game_state["game_board"]
    current_player_index = game_state["turn"]

    for row in range(len(game_board) - 1, -1, -1):
        if game_board[row][column] == -1:
            game_board[row][column] = current_player_index
            return row
    return -1  # No col space


def check_win(game_board, row, col, player_idx):
    #             right  down diagonal-right diagonal-left
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

    def check_direction(dx, dy):
        winning_cells = [(row, col)]
        count = 1
        r, c = row, col
        while (
            0 <= r < len(game_board)
            and 0 <= c < len(game_board[0])
            and game_board[r][c] == player_idx
        ):
            r, c = r + dx, c + dy
            if (
                0 <= r < len(game_board)
                and 0 <= c < len(game_board[0])
                and game_board[r][c] == player_idx
            ):
                winning_cells.append((r, c))
                count += 1
        return count, winning_cells

    for dx, dy in directions:
        count1, cells1 = check_direction(dx, dy)
        count2, cells2 = check_direction(-dx, -dy)
        total_count = (
            count1 + count2 - 1
        )  # Subtract 1 to account for the piece just placed
        if total_count >= 4:
            # returning rows, cols of winning_cells so we can highlight it
            return cells1 + cells2

    return []

def get_current_player(game_state):
    return game_state["players"][game_state["turn"]]

def check_draw(game_board):
    for row in game_board:
        for cell in row:
            if cell == -1:
                return False
    return True


def switch_turn(game_state):
    # just 1 - game_state for
    # e.g 1 - 0 = 1 | 1 - 1 -> 0
    game_state["turn"] = 1 - game_state["turn"]
