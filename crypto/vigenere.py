from helpers import alphabet_position, get_alphabet, rotate_character

def encrypt(text,key):
    key_str = ""

    len_key = len(key)
    len_text = len(text)
    repeat_count = int(len_text/len_key)
    repeat_remainder = int(len_text % len_key)

    for i in range(0,repeat_count):
        key_str = key_str + key

    for i in range(0,repeat_remainder):
        key_str = key_str + key[i]

    count_specials = 0
    new_str = ""
    for i in range(0,len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                new_str = new_str + key_str[i-count_specials].upper()
            else:
                new_str = new_str + key_str[i-count_specials]
        else:
            count_specials = count_specials + 1
            new_str = new_str + " "


    encrypted_str = ''
    for i in range(0,len(text)):
        encrypted_str = encrypted_str + rotate_character(text[i], alphabet_position(new_str[i]) )
    return encrypted_str



def main():
    text = "a"
    print (text)
    print (encrypt(text,'boom'))

if __name__ == '__main__':
    main()
