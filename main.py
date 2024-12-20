import os
import keyboard

# pyinstaller --onefile --windowed --icon=icon_transparent.ico --name="ShortMoji" main.py

# Variable to store the last pressed keys
buffer = []

# Function to be called to when we want to replace the text with an emoji
def replace_with_emoji(emoji: str):
    # Delete the last 5 characters
    for _ in range(5):
        keyboard.press_and_release("backspace")
    # Insert the emoji
    keyboard.write(f"{emoji} ")

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
        # Keep only the last 5 characters
        if len(buffer) > 5:
            buffer.pop(0)
        # Close the program if the user clicks 2 times on the escape key
        if buffer[-2::] == ["esc", "esc"]:
            os._exit(0)
        # Check if the buffer ends with our shortcuts
        match buffer:
            case [":", "l", "a", "u", "space"]:
                replace_with_emoji("😆")
            case [":", "r", "o", "f", "space"]:
                replace_with_emoji("🤣")
            case [":", "s", "l", "i", "space"]:
                replace_with_emoji("🙂")
            case [":", "w", "i", "n", "space"]:
                replace_with_emoji("😉")
            case [":", "i", "n", "n", "space"]:
                replace_with_emoji("😇")
            case [":", "s", "m", "i", "space"]:
                replace_with_emoji("😃")
            case [":", "g", "r", "i", "space"]:
                replace_with_emoji("😁")
            case [":", "s", "w", "e", "space"]:
                replace_with_emoji("😅")
            case [":", "j", "o", "y", "space"]:
                replace_with_emoji("😂")
            case [":", "u", "p", "s", "space"]:
                replace_with_emoji("🙃")
            case [":", "b", "l", "u", "space"]:
                replace_with_emoji("😊")
            case [":", "3", "h", "e", "space"]:
                replace_with_emoji("🥰")
            case [":", "s", "t", "a", "space"]:
                replace_with_emoji("🤩")
            case [":", "t", "e", "a", "space"]:
                replace_with_emoji("🥲")
            case [":", "k", "i", "s", "space"]:
                replace_with_emoji("😘")
            case [":", "y", "u", "m", "space"]:
                replace_with_emoji("😋")
            case [":", "s", "t", "u", "space"]:
                replace_with_emoji("😜")
            case [":", "z", "a", "n", "space"]:
                replace_with_emoji("🤪")
            case [":", "m", "o", "n", "space"]:
                replace_with_emoji("🤑")
            case [":", "h", "u", "g", "space"]:
                replace_with_emoji("🤗")
            case [":", "s", "h", "u", "space"]:
                replace_with_emoji("🤫")
            case [":", "h", "a", "n", "space"]:
                replace_with_emoji("🤭")
            case [":", "t", "h", "i", "space"]:
                replace_with_emoji("🤔")
            case [":", "z", "i", "p", "space"]:
                replace_with_emoji("🤐")
            case [":", "n", "e", "u", "space"]:
                replace_with_emoji("😐")
            case [":", "n", "o", "m", "space"]:
                replace_with_emoji("😶")
            case [":", "r", "o", "l", "space"]:
                replace_with_emoji("🙄")
            case [":", "f", "a", "c", "space"]:
                replace_with_emoji("😮‍💨")
            case [":", "r", "a", "i", "space"]:
                replace_with_emoji("🤨")
            case [":", "u", "n", "a", "space"]:
                replace_with_emoji("😒")
            case [":", "l", "y", "i", "space"]:
                replace_with_emoji("🤥")
            case [":", "r", "e", "l", "space"]:
                replace_with_emoji("😌")
            case [":", "s", "l", "e", "space"]:
                replace_with_emoji("😴")
            case [":", "p", "e", "n", "space"]:
                replace_with_emoji("😔")
            case [":", "d", "r", "o", "space"]:
                replace_with_emoji("🤤")
            case [":", "m", "a", "s", "space"]:
                replace_with_emoji("😷")
            case [":", "b", "a", "n", "space"]:
                replace_with_emoji("🤕")
            case [":", "v", "o", "m", "space"]:
                replace_with_emoji("🤮")
            case [":", "h", "o", "t", "space"]:
                replace_with_emoji("🥵")
            case [":", "w", "o", "o", "space"]:
                replace_with_emoji("🥴")
            case [":", "s", "p", "i", "space"]:
                replace_with_emoji("😵‍💫")
            case [":", "t", "h", "e", "space"]:
                replace_with_emoji("🤒")
            case [":", "n", "a", "u", "space"]:
                replace_with_emoji("🤢")
            case [":", "s", "n", "e", "space"]:
                replace_with_emoji("🤧")
            case [":", "c", "o", "l", "space"]:
                replace_with_emoji("🥶")
            case [":", "d", "i", "z", "space"]:
                replace_with_emoji("😵")
            case [":", "e", "x", "p", "space"]:
                replace_with_emoji("🤯")
            case [":", "c", "o", "w", "space"]:
                replace_with_emoji("🤠")
            case [":", "d", "i", "s", "space"]:
                replace_with_emoji("🥸")
            case [":", "p", "a", "r", "space"]:
                replace_with_emoji("🥳")
            case [":", "s", "u", "n", "space"]:
                replace_with_emoji("😎")
            case [":", "n", "e", "r", "space"]:
                replace_with_emoji("🤓")
            case [":", "c", "o", "n", "space"]:
                replace_with_emoji("😕")
            case [":", "o", "p", "e", "space"]:
                replace_with_emoji("😮")
            case [":", "a", "s", "t", "space"]:
                replace_with_emoji("😲")
            case [":", "p", "l", "e", "space"]:
                replace_with_emoji("🥺")
            case [":", "a", "n", "g", "space"]:
                replace_with_emoji("😧")
            case [":", "c", "r", "y", "space"]:
                replace_with_emoji("😢")
            case [":", "s", "c", "r", "space"]:
                replace_with_emoji("😱")
            case [":", "p", "e", "r", "space"]:
                replace_with_emoji("😣")
            case [":", "t", "i", "r", "space"]:
                replace_with_emoji("😫")
            case [":", "w", "o", "r", "space"]:
                replace_with_emoji("😟")
            case [":", "f", "r", "o", "space"]:
                replace_with_emoji("☹️")
            case [":", "h", "u", "s", "space"]:
                replace_with_emoji("😯")
            case [":", "f", "l", "u", "space"]:
                replace_with_emoji("😳")
            case [":", "f", "e", "a", "space"]:
                replace_with_emoji("😨")
            case [":", "s", "o", "b", "space"]:
                replace_with_emoji("😭")
            case [":", "w", "e", "a", "space"]:
                replace_with_emoji("😩")
            case [":", "y", "a", "w", "space"]:
                replace_with_emoji("🥱")
            case [":", "t", "r", "i", "space"]:
                replace_with_emoji("😤")
            case [":", "s", "k", "u", "space"]:
                replace_with_emoji("💀")
            case [":", "p", "o", "u", "space"]:
                replace_with_emoji("😡")
            case [":", "c", "u", "r", "space"]:
                replace_with_emoji("🤬")
            case [":", "i", "m", "p", "space"]:
                replace_with_emoji("👿")
            case [":", "c", "r", "o", "space"]:
                replace_with_emoji("☠️")
            case [":", "p", "o", "o", "space"]:
                replace_with_emoji("💩")
            case [":", "o", "g", "r", "space"]:
                replace_with_emoji("👹")
            case [":", "g", "h", "o", "space"]:
                replace_with_emoji("👻")
            case [":", "i", "n", "v", "space"]:
                replace_with_emoji("👾")
            case [":", "c", "l", "o", "space"]:
                replace_with_emoji("🤡")
            case [":", "g", "o", "b", "space"]:
                replace_with_emoji("👺")
            case [":", "a", "l", "i", "space"]:
                replace_with_emoji("👽")
            case [":", "r", "o", "b", "space"]:
                replace_with_emoji("🤖")
            case [":", "c", "s", "m", "space"]:
                replace_with_emoji("😺")
            case [":", "c", "j", "o", "space"]:
                replace_with_emoji("😹")
            case [":", "c", "s", "c", "space"]:
                replace_with_emoji("🙀")
            case [":", "c", "p", "o", "space"]:
                replace_with_emoji("😾")
            case [":", "c", "h", "e", "space"]:
                replace_with_emoji("😻")
            case [":", "c", "k", "i", "space"]:
                replace_with_emoji("😽")
            case [":", "c", "c", "r", "space"]:
                replace_with_emoji("😿")
            case [":", "s", "e", "e", "space"]:
                replace_with_emoji("🙈")
            case [":", "s", "p", "e", "space"]:
                replace_with_emoji("🙊")
            case [":", "h", "e", "a", "space"]:
                replace_with_emoji("❤️")
            case [":", "t", "u", "p", "space"]:
                replace_with_emoji("👍")
            case [":", "p", "r", "a", "space"]:
                replace_with_emoji("🙏")
            case [":", "g", "o", "a", "space"]:
                replace_with_emoji("🐐")
            case [":", "f", "i", "r", "space"]:
                replace_with_emoji("🔥")
            case [":", "m", "o", "y", "space"]:
                replace_with_emoji("🗿")
            case [":", "s", "p", "a", "space"]:
                replace_with_emoji("✨")

# Register the keyboard hook
keyboard.hook(on_key)

# Keep the script running
keyboard.wait()