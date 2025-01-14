import json
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys, os
import pystray
from PIL import Image
import webbrowser

# pyinstaller --onefile --windowed --icon=img/icon.ico --name="ShortMoji" --add-data "emojis.json:." --add-data "img/icon_transparent.png:img" main.py

# Dynamic path
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# Create the tray icon
icon_path = os.path.join(base_path, 'img/icon_transparent.png')
image = Image.open(icon_path)

def after_click(icon, query):
    if str(query) == "Github Repository":
        webbrowser.open("https://github.com/TooFuW/ShortMoji")
    elif str(query) == "Exit":
        kboard.tap(Key.esc)
        kboard.tap(Key.esc)
        icon.stop()

icon = pystray.Icon("ShortMoji", image, "ShortMoji", menu=pystray.Menu(
	pystray.MenuItem("Github Repository", after_click),
	pystray.MenuItem("Exit", after_click)))

icon.run_detached()

# Variable to store the last pressed keys
buffer = []

# Initialize the keyboard controller
kboard = Controller()

# Get the emojis list
json_path = os.path.join(base_path, 'emojis.json')
with open(json_path, "r", encoding="utf-8") as file:
    emojis = json.load(file)

# Function to be called to when we want to replace the text with an emoji
def replace_with_emoji(emoji):
    global buffer
    # Delete the last 5 characters
    for _ in range(len(buffer)):
        kboard.tap(Key.backspace)
    # Insert the emoji
    pyperclip.copy(emoji)
    pyautogui.hotkey('ctrl', 'v')
    # Clear the buffer
    buffer = []

# Function to be called when a key is pressed
def on_press(key):
    global buffer
    try:
        # Getting the key when it's a simple character (like "a", "b", "c", "!"...)
        if len(str(key.char)) == 1:
            buffer.append(str(key.char))
    except:
        try:
            # Getting the key when it's a control/modifier key that why may be using later in the function
            if str(key.name) in ["space", "backspace", "esc"]:
                buffer.append(str(key.name))
        except:
            return
    # The backspace key deletes the last character (plus itself) in the buffer
    if len(buffer) > 1 and buffer[-1] == "backspace":
        buffer.pop()
        buffer.pop()
    elif len(buffer) > 0 and buffer[-1] == "backspace":
        buffer.pop()
    # Keep only up to 7 characters if it looks like a shortcut
    if len(buffer) > 7 or (len(buffer) > 0 and (buffer[0] != ":" and buffer[0] != "esc")):
        buffer = []
    # Close the program if the user clicks 2 times on the escape key
    if buffer[-2::] == ["esc", "esc"]:
        icon.stop()
        return False
    # Check if the buffer ends with one of the shortcuts
    if len(buffer) > 0 and buffer[-1] == "space":
        comparaison = "".join(buffer[:-1])
        try:
            replace_with_emoji(emojis[comparaison])
        except Exception as e:
            pass

# Collect keyboard events until on_press returns False
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()