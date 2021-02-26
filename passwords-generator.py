import os
import random

def pass_generate(pass_number, pass_len):
    chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
             '!', '@', '$', '%', '&', '*', '(', ')', '-', '+', '?', '#', 
             'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    x = 0
    while (x < pass_number):
        password = ""
        i = 0
        while (i < pass_len):
            password = password +  chars[random.randint(0,len(chars) - 1)]
            i = i + 1
        x = x + 1
    return(password)

def main():
    pass_number = 1
    pass_len = 32

    # save_file = pass_generate(pass_number, pass_len)
    print(pass_generate(pass_number, pass_len))

    # if (save == "YES" or save == "Y"):
    #     pass_file = open("pwd_generator.txt", "w")
    #     file = pass_file.write(save_file)
    #     pass_file.close()
    #     print("The passwords has been saved in the file \033[1;32;40m'pwd_generator.txt'\033[0;37;40m :)")


if __name__ == '__main__':
    main()
