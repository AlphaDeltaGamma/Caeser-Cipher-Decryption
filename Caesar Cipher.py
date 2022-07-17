def encrypt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + key) % 26
def encrypt_message(message, key):
    message = message.upper()
    cipher = ''
    for char in message:
        if char not in ' ,.':
            cipher += encrypt_char(char, key)
        else:
            cipher += char
    return cipher
encrypt_message("you are awesome.", 3)
def decrypt_char(char, key):
    return chr(ord('A') + (ord(char) - ord('A') + 26 - key) % 26)
def decrypt_message(cipher, key):
    cipher = cipher.upper()
    message = ''
    for char in cipher:
        if char not in ' ,.':
            message += decrypt_char(char, key)
        else:
            message += char
    return message
decrypt_message('BRX DUH DZHVRPH.', 3)               
               
               
     
     
     
