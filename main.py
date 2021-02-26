import os, sys
import random
import eel

eel.init('web')

def close_callback(arg1, arg2):
    sys.exit()

@eel.expose()
def pass_generate(pass_number, pass_len):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
             '!', '@', '$', '%', '&', '*', '(', ')', '-', '+', '?', '#', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = 0
    print(pass_len)
    while (x < pass_number):
        password = ""
        i = 0
        while (i < int(pass_len)):
            password = password +  chars[random.randint(0,len(chars) - 1)]
            i = i + 1
        x = x + 1
    eel.showPassword(password)


# start EEL App
if __name__ == '__main__':
    size = (800,720) #size of App Window
    app_options = {
      'mode' : "chrome",
      'close_callback' : close_callback
    }
    eel.start('index.html', options=app_options, size=size, suppress_error=True)
