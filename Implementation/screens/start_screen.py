import curses
import warnings
import time

from assets.ascii import ascii
from utils.ui import add_multi_line_str
from utils.ansi import add_img_with_ansi



def render_start_screen(win, state=None):
    win.nodelay(True)
    toggle = False
    height, width = win.getmaxyx()
    if height < 25:
        warnings.warn("Please zoom out your terminal. There's not enough space")
        return

    txt_height = 6
    pad = min((height - 4 * txt_height) // 5, 3)

    y = pad
    x = pad if pad + 105 < width else 0

    menu = [
        {"key": "PLAY", "y": y + txt_height + pad, "x": x},
        {"key": "PLAY_COMP", "y": y + 2*(txt_height + pad), "x": x},
        {"key": "HOW_TO_PLAY", "y": y + 3*(txt_height + pad), "x": x},
    ]
    menu_focus = 0

    def clr_prev_focus():
        add_multi_line_str(win, menu_item["y"], menu_item["x"], ascii[menu_item["key"]])
        win.refresh()

    def render_info_text():
        win.addstr(1, width - 30, "Move   -> Use ARROW KEYS", curses.color_pair(12))
        win.addstr(2, width - 30, "Select -> Press ENTER", curses.color_pair(12))
        win.addstr(3, width - 30, "Quit   -> PRESS q", curses.color_pair(11))

    def render_menu():
        for index, item in enumerate(menu):
            add_multi_line_str(win, item["y"], item["x"], ascii[item["key"]])


    frames = 8 # For background
    fr_counter = 0
    while True:
        # animate background
        add_img_with_ansi(f"assets/CF/CF-{fr_counter}.png", width//3, height//4, 2*width//3, win)
        fr_counter += 1
        fr_counter %= frames

        render_menu()
        # animate logo & menu
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

        render_info_text()

        win.refresh()
        toggle = not toggle
        start_time = time.time()

        # add animation delay
        delay = 0.6

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

