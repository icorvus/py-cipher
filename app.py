import string


def caesar_cipher(secret, shift_factor):
    shift_factor %= 26 # There are 26 letters in latin alphabeth
    output_string = ""
    for char in secret:
        if char in string.ascii_lowercase:
            char_unicode = ord(char) + shift_factor
            if char_unicode > 122: # 122 is unicode for "z"
                char_unicode -= 26
            char = chr(char_unicode)

        if char in string.ascii_uppercase:
            char_unicode = ord(char) + shift_factor
            if char_unicode > 90: # 90 is unicode for "Z"
                char_unicode -= 26
            char = chr(char_unicode)
            
        output_string += char
    return output_string


def main():
    print(caesar_cipher("Very secret message!!", 23))
    # Decrypting works by providing the key as negative value
    print(caesar_cipher("Sbov pbzobq jbppxdb!!", -23))

if __name__ == "__main__":
    main()
    