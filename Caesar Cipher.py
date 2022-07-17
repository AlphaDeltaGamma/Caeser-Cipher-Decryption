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
               
     
     
     
