def alphabet_position(letter):
    alphalower = 'abcdefghijklmnopqrstuvwxyz'
    alphaupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #return alphalower.index(letter)
    if letter.isalpha() == False:
        return letter
    index=0
    if letter.islower():
        index = alphalower.index(letter)
    else:
        index=alphaupper.index(letter)
    return index

def get_alphabet(index,char) :
    new_char=""
    alphalower = 'abcdefghijklmnopqrstuvwxyz'
    alphaupper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if char.isalpha() == False:
        return char

    if char.islower():
        new_char = alphalower[index]
    else:
        new_char = alphaupper[index]

    return new_char

def rotate_character(char, rot):
    encrypted = ''
    if char.isalpha() == False:
        return char
    else:
        rotated_index = alphabet_position(char) + rot
        if rotated_index < 26:
            encrypted = get_alphabet(rotated_index,char)
        else:
            encrypted = get_alphabet(rotated_index % 26,char)

    return encrypted

def user_input_is_valid(cl_args):
    if len(cl_args) < 2:
        return False
    if cl_args[1].isdigit() == False:
        return False
    else:
        return True
