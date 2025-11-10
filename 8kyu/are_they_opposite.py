# Give you two strings: s1 and s2. If they are opposite, return true; otherwise, return false. Note: The result should be a boolean value, instead of a string.
#
# The opposite means: All letters of the two strings are the same, but the case is opposite. you can assume that the string only contains letters or it's a empty string. Also take note of the edge case - if both strings are empty then you should return false/False.
#
# Examples (input -> output)
# "ab","AB"     -> true
# "aB","Ab"     -> true
# "aBcd","AbCD" -> true
# "AB","Ab"     -> false
# "",""         -> false
def is_opposite(s1,s2):
    if not s1 or not s2:
        return False
    else:
        for s1_char, s2_char in zip(s1, s2):
            if s1_char.lower() == s2_char.lower() and s1_char == s2_char:
                return  False
        return True