from pynput import keyboard

def on_press(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def on_release(key):
    print(f"Key released: {key}")

    # Stop when ESC is pressgmed
    if key == keyboard.Key.esc:
        print("Program stopped.")
        return False

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release
) as listener:
    print("Press keys (ESC to exit)...")
    listener.join()