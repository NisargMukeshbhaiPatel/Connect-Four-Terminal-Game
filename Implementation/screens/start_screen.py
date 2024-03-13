import curses
import warnings
import time

from assets.ascii import ascii
from utils.ui import add_multi_line_str


def render_start_screen(win, state=None):
    win.nodelay(True)
    toggle = False
    height, width = win.getmaxyx()
    if height < 25:
        warnings.warn("Please zoom out your terminal. There's not enough space")
        return

    pad = height // 12
    txt_height = 6

    y = pad
    x = pad if pad + 105 < width else 0

    menu = [
        {"key": "PLAY", "y": y + txt_height + pad, "x": x},
        {"key": "HOW_TO_PLAY", "y": y + 2*(txt_height + pad), "x": x},
    ]
    menu_focus = 0

    def clr_prev_focus():
        add_multi_line_str(win, menu_item["y"], menu_item["x"], ascii[menu_item["key"]])
        win.refresh()

    add_multi_line_str(win, menu[0]["y"], menu[0]["x"], ascii["PLAY"])
    add_multi_line_str(win, menu[1]["y"], menu[1]["x"], ascii["HOW_TO_PLAY"])

    while True:
        menu_item = menu[menu_focus]
        if toggle:
            add_multi_line_str(
                win,
                y,
                x,
                ascii["CONNECT_FOUR_LOGO2"],
                color=curses.color_pair(16),
            )
            add_multi_line_str(
                win,
                menu_item["y"],
                menu_item["x"],
                ascii[menu_item["key"] + "2"],
                color=curses.color_pair(16),
            )
        else:
            add_multi_line_str(
                win,
                y,
                x,
                ascii["CONNECT_FOUR_LOGO"],
                color=curses.color_pair(13),
            )
            add_multi_line_str(
                win,
                menu_item["y"],
                menu_item["x"],
                ascii[menu_item["key"]],
                color=curses.color_pair(13),
            )

        win.refresh()
        toggle = not toggle
        start_time = time.time()
        delay = 0.5

        while time.time() - start_time < delay:
            key = win.getch()
            if key == curses.KEY_DOWN:
                clr_prev_focus()
                menu_focus += 1
                menu_focus %= len(menu)
                break

            elif key == curses.KEY_UP:
                clr_prev_focus()
                menu_focus -= 1
                if menu_focus < 0:
                    menu_focus += len(menu)
                break

            elif key == curses.KEY_ENTER or key == 10 or key == 459:
                return menu[menu_focus]["key"], None

            elif key == ord("q") or key == ord("Q"):
                return

