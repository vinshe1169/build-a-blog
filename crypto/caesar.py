from helpers import alphabet_position, get_alphabet, rotate_character,user_input_is_valid
from sys import argv,exit
import string

def encrypt(text, rot):
    rtn_str = ""
    for i in range(len(text)):
        rtn_str = rtn_str + rotate_character(text[i],rot)
    return rtn_str

def main():
    if user_input_is_valid(argv) == False:
        print("Usage: Caesar.py n")
        exit()
    rot_num = int(argv[1])
    msg = raw_input ("Type a message:" )
    print(encrypt(msg, rot_num))

if __name__ == '__main__':
    main()
