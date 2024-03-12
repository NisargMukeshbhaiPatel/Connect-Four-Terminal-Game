import curses
from ascii_magic import AsciiArt

# ANSI color codes from 30-37
ANSI_COLORS = (
	curses.COLOR_BLACK,  # 30
	curses.COLOR_RED,
	curses.COLOR_GREEN,
	curses.COLOR_YELLOW,
	curses.COLOR_BLUE,
	curses.COLOR_MAGENTA,
	curses.COLOR_CYAN,
	curses.COLOR_WHITE,  # 37
)

def set_init_pair_ansi_index():
	curses.use_default_colors()
	# Set pairs according to ANSI_COLORS idx
	# For 0, it's set to default background color of terminal and also curses doesn't allow setting it
	for i in range(1, 8):
		curses.init_pair(i, -1, ANSI_COLORS[i])


