#!/usr/bin/env python3

def caesarCipherEncryptor(string, key):
    '''
        Time: N
        Space: N
    '''
    encrypted_list = []
    for char in string:
        char_int = ord(char) - 97
        char_int += key
        char_int %= 26
        enc_int = char_int + 97
        encrypted_list.append(chr(enc_int))
    return ''.join(encrypted_list)
