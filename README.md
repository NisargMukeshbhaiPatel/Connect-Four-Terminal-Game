# Connect Four

Connect Four is a classic two-player game in which the players take turns dropping colored discs into a grid. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs.

# Gameplay Clip
![cf](https://github.com/NisargMukeshbhaiPatel/Connect-Four-Terminal-Game/assets/101616954/3c26dd5d-08d1-4f1e-b7a1-b6446d94969b)

## Installation

**NOTE**: Use a Python version **< 3.12** if you're on Windows, as there is an issue with the `windows-curses` module. See [windows-curses issue#48](https://github.com/zephyrproject-rtos/windows-curses/issues/48)

1. **Clone & Install dependencies:**

   ```bash
	git clone https://github.com/NisargMukeshbhaiPatel/Connect-Four-Terminal-Game.git
	cd Connect-Four-Terminal-Game/Implementation
	pip install -r requirements.txt
   ```

2. **Run Code:**

   ```bash
	python main.py	
   ```

## Building Executable
An Example build for Windows x86_64 is already provided for reference

Follow these steps to build a single executable file

```bash
pip install pyinstaller
cd Implementation
pyinstaller --onefile main.py
```

Copy the `assets/` folder to the `dist/` so executable can access assets

Find your build file inside the `dist/` folder and run it

## Troubleshooting

If you encounter issues with pyinstaller or pip not being found, try the following:

```bash
python -m pip install pyinstaller
python -m PyInstaller --onefile main.py 
# OR
py -m pip install pyinstaller
py -m PyInstaller --onefile main.py 
```

