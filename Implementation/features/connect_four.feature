Feature: Connect Four Game in Terminal

    Scenario: Game window initializes correctly
        Given a new Connect Four game
        Then the game should display the start screen menu

	Scenario: Game starts correctly with empty board
        Given a Connect Four game with player1 and player2
        Then the game board should be empty


	Scenario: Players switch turns dropping pieces
        Given a Connect Four game with player1 and player2
        When player1 drops a piece in column 1
        Then it should be player2 turn


	Scenario: Taking Turns - Player vs Computer 
        Given a Connect Four game with player1 and computer
        When player1 drops a piece in column 3
        Then it should be computer turn
        When the computer automatically drops a piece
        Then the computer should drop a piece in a valid column on the game board
        And it should be player1 turn


	Scenario: Game ends in a draw
        # 0 is for player 1 and X is for player 2, we've used to show moves
        Given a Connect Four game with players player1 and player2
        When players drop pieces on the game board in the following pattern
			"""
			X 0 0 0 X 0 X
			0 X X X 0 X 0
			X 0 0 0 X 0 X
			0 X X X 0 X 0
			X 0 0 0 X 0 X
			0 X X X 0 X 0
			"""
        Then the game should end in a draw

	Scenario: Player wins diagonally
        Given a Connect Four game with players player1 and player2
        When players drop pieces on the game board in the following pattern
			"""
			- - - - - - -
			- - - - - - -
			- - - - - - X
			- - - - - X 0
			- - - - X 0 0
			- 0 0 X 0 0 0
			"""
		Then player2 should win the game with the last dropped row 3 and column 7

	Scenario: Player wins horizontally
        Given a Connect Four game with players player1 and player2
        When players drop pieces on the game board in the following pattern
			"""
			- - - - - - -
			- - - - - - -
			- - - - - - X
			- - - - - X 0
			- - - - X X 0
			- 0 0 0 0 X 0
			"""
		Then player1 should win the game with the last dropped row 6 and column 2

	Scenario: Player wins vertically
        Given a Connect Four game with players player1 and player2
        When players drop pieces on the game board in the following pattern
			"""
			- - - - - - -
			- - - - - - -
			- - - - - X X
			- - - - - X 0
			- - - - X X 0
			- X 0 0 0 X 0
			"""
		Then player2 should win the game with the last dropped row 3 and column 6

	Scenario: Invalid Move when column is full
        Given a Connect Four game with players player1 and player2
        When players drop pieces on the game board in the following pattern
			"""
			- - - - - - X
			- - - - - - X
			- - - - - 0 X
			- - - - - X 0
			- - - - X X 0
			- X 0 0 0 X 0
			"""
	    Then dropping a piece in column 7 should return -1

