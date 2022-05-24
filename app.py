import string


def caesar_cipher(secret, shift_factor):
    shift_factor %= 26
    output_string = ""
    for char in secret:
        if char in string.ascii_lowercase:
            char_unicode = ord(char) + shift_factor
            if char_unicode > 122:
                char_unicode -= 26
            char = chr(char_unicode)

        if char in string.ascii_uppercase:
            char_unicode = ord(char) + shift_factor
            if char_unicode > 90:
                char_unicode -= 26
            char = chr(char_unicode)
            
        output_string += char
    return output_string


def main():
    pass

if __name__ == "__main__":
    main()
    