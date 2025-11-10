def detect_sequence(index, char_to_find, word):
    count = 0
    for char in word[index:]:
        if char_to_find != char:
            break
        else:
            count+= 1
    return count

def decode_bits(bits):
    i = 0
    morse_code = ""
    print(bits)
    while i < len(bits):
        char = bits[i]
        count = detect_sequence(i, char, bits)
        i += count
        if char.isnumeric():

            # One or a 2 is a dot, but 3 is a dash
            if count > 7 and int(char) == 0:
                morse_code += "   "
            elif count > 3:
                morse_code += "-" if int(char) == 1 else " "
            elif count == 2 or count == 1 or count == 3:
                morse_code += "." if int(char) == 1 else ""

        else:
            print(char, "not numeric")
    return morse_code

print("--- answer ---",decode_bits("111000000000111"))