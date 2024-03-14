import curses

from utils.ansi import set_init_pair_ansi_index
from screens.start_screen import render_start_screen
from screens.game_screen import render_game_screen
from screens.tutorial_screen import render_tutorial_screen


screen_map = {
    "START": render_start_screen,
    "PLAY": render_game_screen,
    "PLAY_COMP": render_game_screen,
    "HOW_TO_PLAY": render_tutorial_screen,
}


def main(stdscr):
    curses.curs_set(0)
    stdscr.keypad(True)
    set_init_pair_ansi_index()

    # Handle Screen routing
    current_screen = "START"
    state = None  # To pass state between screens
    while True:
        stdscr.clear()
        stdscr.refresh()
        render_function = screen_map[current_screen]
        result = render_function(stdscr, state)

        if result:
            current_screen, state = result
        else:
            return


curses.wrapper(main)
