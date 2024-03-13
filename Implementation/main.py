import curses
import time

from utils import ansi, ui
from assets.ascii import ascii

# def add_delay


def main(stdscr):
    curses.curs_set(0)
    ansi.set_init_pair_ansi_index()

    stdscr.nodelay(True)
    toggle = False
    menu = [{"key": "PLAY", "y": 14, "x": 10}, {"key": "HOW_TO_PLAY", "y": 20, "x": 10}]
    menu_focus = 0
    ui.add_multi_line_str(stdscr, 14, 10, ascii["PLAY"])
    ui.add_multi_line_str(stdscr, 20, 10, ascii["HOW_TO_PLAY"])

    while True:
        menu_item = menu[menu_focus]
        if toggle:
            ui.add_multi_line_str(stdscr, 4, 4, ascii["CONNECT_FOUR_LOGO2"])
            ui.add_multi_line_str(
                stdscr, menu_item["y"], menu_item["x"], ascii[menu_item["key"] + "2"]
            )
        else:
            ui.add_multi_line_str(stdscr, 4, 4, ascii["CONNECT_FOUR_LOGO"])
            ui.add_multi_line_str(
                stdscr, menu_item["y"], menu_item["x"], ascii[menu_item["key"]]
            )

        stdscr.refresh()
        toggle = not toggle
        start_time = time.time()
        delay = 0.5

        while time.time() - start_time < delay:
            key = stdscr.getch()
            if key == curses.KEY_DOWN:
                ui.add_multi_line_str(
                    stdscr, menu_item["y"], menu_item["x"], ascii[menu_item["key"]]
                )
                stdscr.refresh()
                menu_focus += 1
                menu_focus %= len(menu)
            elif key == ord("q") or key == ord("Q"):
                return

    # stdscr.getch()


# if curses.has_colors():
# win.attron(curses.color_pair(2))
# win.border()
# win.attron(curses.color_pair(0))
curses.wrapper(main)
