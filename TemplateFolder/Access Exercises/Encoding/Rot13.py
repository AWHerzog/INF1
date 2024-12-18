def rot_n(plain_text, shift_by):
    result = ""

    for char in plain_text:
        if char.isupper() and char.isalpha():
            ascii_code = ord(char)
            position = (ascii_code - 65 + shift_by) % 26
            result += chr(position + 65)
        elif char.islower() and char.isalpha():
            ascii_code = ord(char)
            position = (ascii_code -97 + shift_by) %26
            result += chr(position + 97)
        else:
            result += char
    # Make sure to return the correct result!
    return result

print(rot_n("abc", 1))