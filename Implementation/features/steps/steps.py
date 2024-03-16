from behave import given, when, then
from game.game_logic import (
    create_connect_four_game,
    drop_piece,
    get_current_player,
    check_win,
    check_draw,
    switch_turn,
)
from game.game_ai import get_computer_move_rand


# Scenario: Game window initializes correctly
@given("a new Connect Four game")
def create_new_game(context):
    pass


@then("the game should display the start screen menu")
def check_start_screen(context):
    pass


# Scenario: Game starts correctly with empty board
@given("a Connect Four game with {player1} and {player2}")
def step_new_game_with_players(context, player1, player2):
    context.game_state = create_connect_four_game(player1, "red", player2, "yellow")


@then("the game board should be empty")
def check_empty_board(context):
    assert all(
        all(cell == -1 for cell in row) for row in context.game_state["game_board"]
    )


# Scenario: Players switch turns dropping pieces
@when("{player_name} drops a piece in column {column}")
def player_drops_piece(context, player_name, column):
    game_state = context.game_state
    for i, player in enumerate(game_state["players"]):
        if player["name"] == player_name:
            game_state["turn"] = i
    column = int(column) - 1
    drop_piece(game_state, column)
    switch_turn(game_state)


@then("it should be {player_name} turn")
def step_check_players_turn(context, player_name):
    current_turn_player = context.game_state["players"][context.game_state["turn"]]
    assert current_turn_player["name"] == player_name


# Scenario: Taking Turns - Player vs Computer
# Given, When and Then are implemented above
@when("the computer automatically drops a piece")
def step_impl(context):
    #TODO
    switch_turn(context.game_state)


@then("the computer should drop a piece in a valid column on the game board")
def step_impl(context):
    pass


# Scenario: Game ends in a draw
@then("the game should end in a draw")
def check_draw_game(context):
    game_board = context.game_state["game_board"]
    assert check_draw(game_board)


# winninig Scenarios
@when('players drop pieces on the game board in the following pattern')
def step_drop_pieces_on_board(context):
    game_board = parse_game_board(context.text)
    # Now you can iterate over the game_board and drop pieces accordingly
    for i, row in enumerate(game_board):
        for j, cell in enumerate(row):
            if cell == "X":
                game_board[i][j] = 1
            elif cell == "0":
                game_board[i][j] = 0
            elif cell == "-":
                game_board[i][j] = -1 
    context.game_state["game_board"] = game_board


@then("{name} should win the game with the last dropped row {r} and column {c}")
def check_winning(context, name, r, c):
    game_state = context.game_state
    for i, player in enumerate(game_state["players"]):
        if player["name"] == name:
            game_state["turn"] = i
    assert check_win(
        game_state["game_board"], int(r)-1, int(c)-1, game_state["turn"]
    )


# Scenario: Invalid Move when column is full
@then("dropping a piece in column {column} should return {return_value}")
def check_invalid_move(context, column, return_value):
    column = int(column) - 1
    assert drop_piece(context.game_state, column) == int(return_value)


# utils functions
def parse_game_board(game_board_str):
    rows = game_board_str.strip().split("\n")
    game_board = []
    for row in rows:
        game_board.append(row.split())
    return game_board

