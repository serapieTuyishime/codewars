def detect_sequence(index, char_to_find, word):
    count = 0
    for char in word[index:]:
        if char_to_find != char:
            break
        else:
            count += 1
    return count


def decode_bits(bits):
    bits = bits.strip('0')

    if not bits:
        return ""

    time_unit = len(bits)
    i = 0
    while i < len(bits):
        count = detect_sequence(i, bits[i], bits)
        time_unit = min(time_unit, count)
        i += count

    morse_code = ""
    i = 0

    while i < len(bits):
        char = bits[i]
        count = detect_sequence(i, char, bits)
        units = count // time_unit

        if char == '0':
            if units >= 7:
                morse_code += "   "
            elif units >= 3:
                morse_code += " "
        else:
            if units >= 3:
                morse_code += "-"
            else:
                morse_code += "."

        i += count

    return morse_code

print(decode_bits('11111100000011111100000011111100000011111100'
                  '0000000000000000111111000000000000000000111111111111'
                  '11111100000011111100000011111111111111111100000011111111111111111100'
                  '00000000000000000000000000000000000000001111110000001111111111111'
                  '1111100000011111111111111111100000011111111111111111100000000000000000'
                  '011111100000011111100000011111111111111111100000000000000000011111111111'
                  '1111111000000111111000000111111000000000000000000111111'))
