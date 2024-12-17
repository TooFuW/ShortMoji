import os
import keyboard

# pyinstaller --onefile --windowed --icon=icon_transparent.ico --name="ShortMoji" main.py

# Variable to store the last pressed keys
buffer = []

def on_key(event):
    global buffer
    # If the user pressed a key on the keyboard
    if event.event_type == 'down':
        buffer.append(event.name)
        # Keep only the last 4 characters
        if len(buffer) > 4:
            buffer.pop(0)
        print(buffer)
        # Check if the buffer ends with our shortcuts
        match buffer:
            case ["esc", "esc", "esc", "esc"]:
                # Exit the script
                os._exit(0)
            case [":", "r", "o", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('🤣 ')
            case [":", "j", "o", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('😂 ')
            case [":", "s", "o", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('😭 ')
            case [":", "s", "u", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('😎 ')
            case [":", "s", "t", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('🤩 ')
            case [":", "n", "e", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('🤓 ')
            case [":", "f", "i", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('🔥 ')
            case [":", "m", "o", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('🗿 ')
            case [":", "s", "k", "space"]:
                # Remove the last 4 characters from the buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insert the emoji
                keyboard.write('💀 ')
            

# Register the keyboard hook
keyboard.hook(on_key)

# Keep the script running
keyboard.wait()