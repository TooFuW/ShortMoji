import os
import keyboard

# pyinstaller --onefile --windowed --icon=img/icon.ico --name="ShortMoji" main.py

# Variable to store the last pressed keys
buffer = []

# Function to be called to when we want to replace the text with an emoji
def replace_with_emoji(emoji: str):
    global buffer
    # Delete the last 5 characters
    for _ in range(len(buffer)):
        keyboard.press_and_release("backspace") 
    # Insert the emoji
    keyboard.write(f"{emoji} ")
    # Clear the buffer
    buffer = []

# Function to be called when a key is pressed
def on_key(event):
    global buffer
    # If the user pressed a key on the keyboard
    if event.event_type == "down":
        buffer.append(event.name)
        # The backspace key deletes the last character (plus itself)
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
            os._exit(0)
        # Check if the buffer ends with one of the shortcuts
        match buffer:
            case [":", "g", "r", "i", "space"]:
                replace_with_emoji("😀")
            case [":", "s", "m", "i", "space"]:
                replace_with_emoji("😄")
            case [":", "l", "a", "space"]:
                replace_with_emoji("😆")
            case [":", "r", "o", "space"]:
                replace_with_emoji("🤣")
            case [":", "s", "l", "space"]:
                replace_with_emoji("🙂")
            case [":", "w", "i", "space"]:
                replace_with_emoji("😉")
            case [":", "i", "n", "space"]:
                replace_with_emoji("😇")
            case [":", "s", "m", "space"]:
                replace_with_emoji("😃")
            case [":", "g", "r", "space"]:
                replace_with_emoji("😁")
            case [":", "s", "w", "space"]:
                replace_with_emoji("😅")
            case [":", "j", "o", "space"]:
                replace_with_emoji("😂")
            case [":", "u", "p", "space"]:
                replace_with_emoji("🙃")
            case [":", "b", "l", "space"]:
                replace_with_emoji("😊")
            case [":", "3", "h", "space"]:
                replace_with_emoji("🥰")
            case [":", "s", "t", "space"]:
                replace_with_emoji("🤩")
            case [":", "k", "i", "s", "space"]:
                replace_with_emoji("😗")
            case [":", "k", "i", "s", "c", "space"]:
                replace_with_emoji("😚")
            case [":", "t", "e", "space"]:
                replace_with_emoji("🥲")
            case [":", "h", "e", "a", "space"]:
                replace_with_emoji("🥲")
            case [":", "k", "i", "space"]:
                replace_with_emoji("😘")
            case [":", "r", "e", "l", "space"]:
                replace_with_emoji("☺️")
            case [":", "k", "i", "s", "s", "space"]:
                replace_with_emoji("😙")
            case [":", "y", "u", "space"]:
                replace_with_emoji("😋")
            case [":", "s", "t", "u", "w", "space"]:
                replace_with_emoji("😜")
            case [":", "s", "t", "u", "c", "space"]:
                replace_with_emoji("😝")
            case [":", "s", "t", "u", "space"]:
                replace_with_emoji("😛")
            case [":", "z", "a", "space"]:
                replace_with_emoji("🤪")
            case [":", "m", "o", "space"]:
                replace_with_emoji("🤑")
            case [":", "h", "u", "space"]:
                replace_with_emoji("🤗")
            case [":", "s", "h", "space"]:
                replace_with_emoji("🤫")
            case [":", "h", "a", "space"]:
                replace_with_emoji("🤭")
            case [":", "t", "h", "space"]:
                replace_with_emoji("🤔")
            case [":", "z", "i", "space"]:
                replace_with_emoji("🤐")
            case [":", "n", "e", "r", "space"]:
                replace_with_emoji("😐")
            case [":", "n", "o", "space"]:
                replace_with_emoji("😶")
            case [":", "s", "m", "i", "r", "space"]:
                replace_with_emoji("😶")
            case [":", "r", "o", "l", "space"]:
                replace_with_emoji("🙄")
            case [":", "f", "a", "space"]:
                replace_with_emoji("😮‍💨")
            case [":", "r", "a", "space"]:
                replace_with_emoji("🤨")
            case [":", "e", "x", "p", "space"]:
                replace_with_emoji("😑")
            case [":", "f", "a", "c", "space"]:
                replace_with_emoji("😶‍🌫️")
            case [":", "u", "n", "space"]:
                replace_with_emoji("😒")
            case [":", "g", "r", "i", "m", "space"]:
                replace_with_emoji("😬")
            case [":", "l", "y", "space"]:
                replace_with_emoji("🤥")
            case [":", "r", "e", "space"]:
                replace_with_emoji("😌")
            case [":", "s", "l", "e", "e","space"]:
                replace_with_emoji("😪")
            case [":", "s", "l", "e", "space"]:
                replace_with_emoji("😴")
            case [":", "p", "e", "space"]:
                replace_with_emoji("😔")
            case [":", "d", "r", "space"]:
                replace_with_emoji("🤤")
            case [":", "m", "a", "space"]:
                replace_with_emoji("😷")
            case [":", "b", "a", "space"]:
                replace_with_emoji("🤕")
            case [":", "v", "o", "space"]:
                replace_with_emoji("🤮")
            case [":", "h", "o", "space"]:
                replace_with_emoji("🥵")
            case [":", "w", "o", "space"]:
                replace_with_emoji("🥴")
            case [":", "s", "p", "space"]:
                replace_with_emoji("😵‍💫")
            case [":", "t", "h", "e", "space"]:
                replace_with_emoji("🤒")
            case [":", "n", "a", "space"]:
                replace_with_emoji("🤢")
            case [":", "s", "n", "space"]:
                replace_with_emoji("🤧")
            case [":", "c", "o", "space"]:
                replace_with_emoji("🥶")
            case [":", "d", "i", "space"]:
                replace_with_emoji("😵")
            case [":", "e", "x", "space"]:
                replace_with_emoji("🤯")
            case [":", "c", "o", "w", "space"]:
                replace_with_emoji("🤠")
            case [":", "d", "i", "s", "space"]:
                replace_with_emoji("🥸")
            case [":", "p", "a", "space"]:
                replace_with_emoji("🥳")
            case [":", "s", "u", "space"]:
                replace_with_emoji("😎")
            case [":", "n", "e", "space"]:
                replace_with_emoji("🤓")
            case [":", "m", "o", "n", "space"]:
                replace_with_emoji("🧐")
            case [":", "c", "o", "n", "space"]:
                replace_with_emoji("😕")
            case [":", "s", "l", "i", "space"]:
                replace_with_emoji("🙁")
            case [":", "o", "p", "space"]:
                replace_with_emoji("😮")
            case [":", "a", "s", "space"]:
                replace_with_emoji("😲")
            case [":", "p", "l", "space"]:
                replace_with_emoji("🥺")
            case [":", "a", "n", "space"]:
                replace_with_emoji("😧")
            case [":", "c", "o", "l", "space"]:
                replace_with_emoji("😰")
            case [":", "c", "r", "space"]:
                replace_with_emoji("😢")
            case [":", "s", "c", "space"]:
                replace_with_emoji("😱")
            case [":", "p", "e", "r", "space"]:
                replace_with_emoji("😣")
            case [":", "s", "w", "e", "space"]:
                replace_with_emoji("😓")
            case [":", "t", "i", "space"]:
                replace_with_emoji("😫")
            case [":", "w", "o", "r", "space"]:
                replace_with_emoji("😟")
            case [":", "f", "r", "space"]:
                replace_with_emoji("☹️")
            case [":", "h", "u", "s", "space"]:
                replace_with_emoji("😯")
            case [":", "f", "l", "space"]:
                replace_with_emoji("😳")
            case [":", "f", "r", "o", "space"]:
                replace_with_emoji("😦")
            case [":", "f", "e", "space"]:
                replace_with_emoji("😨")
            case [":", "d", "i", "s", "r", "space"]:
                replace_with_emoji("😥")
            case [":", "s", "o", "space"]:
                replace_with_emoji("😭")
            case [":", "c", "o", "n", "f", "space"]:
                replace_with_emoji("😖")
            case [":", "d", "i", "s", "a", "space"]:
                replace_with_emoji("😞")
            case [":", "w", "e", "space"]:
                replace_with_emoji("😩")
            case [":", "y", "a", "space"]:
                replace_with_emoji("🥱")
            case [":", "t", "r", "space"]:
                replace_with_emoji("😤")
            case [":", "a", "n", "g", "space"]:
                replace_with_emoji("😠")
            case [":", "i", "m", "p", "s", "space"]:
                replace_with_emoji("😈")
            case [":", "s", "k", "space"]:
                replace_with_emoji("💀")
            case [":", "p", "o", "space"]:
                replace_with_emoji("😡")
            case [":", "c", "u", "space"]:
                replace_with_emoji("🤬")
            case [":", "i", "m", "space"]:
                replace_with_emoji("👿")
            case [":", "c", "r", "o", "space"]:
                replace_with_emoji("☠️")
            case [":", "p", "o", "o", "space"]:
                replace_with_emoji("💩")
            case [":", "o", "g", "space"]:
                replace_with_emoji("👹")
            case [":", "g", "h", "space"]:
                replace_with_emoji("👻")
            case [":", "i", "n", "v", "space"]:
                replace_with_emoji("👾")
            case [":", "c", "l", "space"]:
                replace_with_emoji("🤡")
            case [":", "g", "o", "b", "space"]:
                replace_with_emoji("👺")
            case [":", "a", "l", "space"]:
                replace_with_emoji("👽")
            case [":", "r", "o", "b", "space"]:
                replace_with_emoji("🤖")
            case [":", "c", "s", "space"]:
                replace_with_emoji("😺")
            case [":", "c", "j", "space"]:
                replace_with_emoji("😹")
            case [":", "c", "s", "m", "space"]:
                replace_with_emoji("😼")
            case [":", "c", "s", "c", "space"]:
                replace_with_emoji("🙀")
            case [":", "c", "p", "space"]:
                replace_with_emoji("😾")
            case [":", "c", "s", "m", "i", "space"]:
                replace_with_emoji("😸")
            case [":", "c", "h", "space"]:
                replace_with_emoji("😻")
            case [":", "c", "k", "space"]:
                replace_with_emoji("😽")
            case [":", "c", "c", "space"]:
                replace_with_emoji("😿")
            case [":", "s", "e", "space"]:
                replace_with_emoji("🙈")
            case [":", "s", "p", "e", "space"]:
                replace_with_emoji("🙊")
            case [":", "h", "e", "a", "r", "space"]:
                replace_with_emoji("🙉")
            case [":", "h", "e", "space"]:
                replace_with_emoji("❤️")
            case [":", "t", "u", "space"]:
                replace_with_emoji("👍")
            case [":", "p", "r", "space"]:
                replace_with_emoji("🙏")
            case [":", "g", "o", "space"]:
                replace_with_emoji("🐐")
            case [":", "f", "i", "space"]:
                replace_with_emoji("🔥")
            case [":", "m", "o", "y", "space"]:
                replace_with_emoji("🗿")
            case [":", "s", "p", "a", "space"]:
                replace_with_emoji("✨")

# Register the keyboard hook
keyboard.hook(on_key)

# Keep the script running
keyboard.wait()