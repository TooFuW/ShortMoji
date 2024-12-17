import keyboard

# pyinstaller --onefile --windowed --icon=icon_transparent.ico --name="ShortMoji" main.py

# Variable pour stocker les dernières touches pressées
buffer = []

def on_key(event):
    global buffer
    # Si l'utilisateur a cliqué sur une touche du clavier
    if event.event_type == 'down':
        buffer.append(event.name)
        # On ne garde que les 4 derniers caractères
        if len(buffer) > 4:
            buffer.pop(0)
        print(buffer)
        # Vérifier si le buffer se termine par nos raccourcis
        match buffer:
            case [":", "r", "o", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('🤣 ')
            case [":", "j", "o", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('😂 ')
            case [":", "s", "o", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('😭 ')
            case [":", "s", "u", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('😎 ')
            case [":", "s", "t", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('🤩 ')
            case [":", "n", "e", "space"]:
                # Supprimer les 4 caractères du buffer
                for _ in range(4):
                    keyboard.press_and_release('backspace')
                # Insérer l'émoji
                keyboard.write('🤓 ')

# Enregistrer le hook clavier
keyboard.hook(on_key)

# Maintenir le script en cours d'exécution
keyboard.wait()