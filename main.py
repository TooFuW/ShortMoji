import os
import keyboard

# pyinstaller --onefile --windowed --icon=icon_transparent.ico --name="ShortMoji" main.py

# Variable to store the last pressed keys
buffer = []

# Function to be called to when we want to replace the text with an emoji
def replace_with_emoji(emoji: str):
    # Delete the last 4 characters
    for _ in range(4):
        keyboard.press_and_release("backspace")
    # Insert the emoji
    keyboard.write(f"{emoji} ")

# Function to be called when a key is pressed
def on_key(event):
    global buffer
    # If the user pressed a key on the keyboard
    if event.event_type == "down":
        buffer.append(event.name)
        # Keep only the last 4 characters
        if len(buffer) > 4:
            buffer.pop(0)
        # Check if the buffer ends with our shortcuts
        match buffer:
            case ["esc", "esc", "esc", "esc"]:
                # Exit the script
                os._exit(0)
            case [":", "r", "o", "space"]:
                replace_with_emoji("🤣")
            case [":", "j", "o", "space"]:
                replace_with_emoji("😂")
            case [":", "s", "o", "space"]:
                replace_with_emoji("😭")
            case [":", "s", "u", "space"]:
                replace_with_emoji("😎")
            case [":", "s", "t", "space"]:
                replace_with_emoji("🤩")
            case [":", "n", "e", "space"]:
                replace_with_emoji("🤓")
            case [":", "f", "i", "space"]:
                replace_with_emoji("🔥")
            case [":", "m", "o", "space"]:
                replace_with_emoji("🗿")
            case [":", "s", "k", "space"]:
                replace_with_emoji("💀")
            case [":", "h", "e", "space"]:
                replace_with_emoji("❤️")
            case [":", "c", "l", "space"]:
                replace_with_emoji("🤡")
            case [":", "d", "r", "space"]:
                replace_with_emoji("🤤")
            case [":", "g", "o", "space"]:
                replace_with_emoji("🐐")
            case [":", "k", "i", "space"]:
                replace_with_emoji("😘")
            case [":", "i", "n", "space"]:
                replace_with_emoji("😇")
            case [":", "s", "w", "space"]:
                replace_with_emoji("😅")
            case [":", "y", "u", "space"]:
                replace_with_emoji("😋")
            case [":", "u", "p", "space"]:
                replace_with_emoji("👍")
            case [":", "p", "r", "space"]:
                replace_with_emoji("🙏")
            case [":", "s", "p", "space"]:
                replace_with_emoji("✨")
            case [":", "3", "h", "space"]:
                replace_with_emoji("🥰")
            case [":", "p", "l", "space"]:
                replace_with_emoji("🥺")

# Register the keyboard hook
keyboard.hook(on_key)

# Keep the script running
keyboard.wait()