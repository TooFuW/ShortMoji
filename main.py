import json
import pyautogui
from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import sys, os

# pyinstaller --onefile --windowed --icon=img/icon.ico --name="ShortMoji" --add-data "emojis.json:." main.py

# Variable to store the last pressed keys
buffer = []

# Initialize the keyboard controller
kboard = Controller()

# Dynamic path for the json
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")
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
    # Getting the key
    try:
        buffer.append(key.char)
    except:
        try:
            buffer.append(key.name)
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
        buffer.pop(0)
    # Close the program if the user clicks 2 times on the escape key
    if buffer[-2::] == ["esc", "esc"]:
        return False
    # Check if the buffer ends with one of the shortcuts
    if len(buffer) > 0 and buffer[-1] == "space":
        comparaison = ""
        for char in buffer[0:-1]:
            comparaison += char
        try:
            replace_with_emoji(emojis[comparaison + " "])
        except Exception as e:
            pass

# Collect keyboard events until on_press returns False
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()