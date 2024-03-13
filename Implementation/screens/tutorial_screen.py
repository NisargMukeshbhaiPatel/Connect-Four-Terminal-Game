import curses
import time

from assets.ascii import ascii
from utils.ui import add_multi_line_str


def render_tutorial_screen(win, state=None):
    win.nodelay(False)
    win.addstr("\n")
    win.addstr("  THIS SCREEN IS NOT IMPLEMENTED YET! PRESS 'q' TO GO BACK")
    key = win.getch()
    if key == ord("q") or key == ord("Q"):
        return "START", None

