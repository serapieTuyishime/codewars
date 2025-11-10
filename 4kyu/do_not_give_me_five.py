
def count_up_to(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    s = str(n)
    length = len(s)
    count = 1


    for i in range(length):
        digit = int(s[i])
        print(digit, "----")
        remaining = length - i - 1

        if i == 0:  # First digit position (can't be 0 for positive numbers)
            # Count all valid numbers with fewer digits than n
            for d in range(1, length):
                count += 8 * (9 ** (d - 1))  # First digit: 1-4,6-9 (8 choices)

            # Count numbers with same number of digits but smaller first digit
            if digit > 5:
                count += 5 * (9 ** remaining)  # First digit can be 1,2,3,4,6
            elif digit == 5:
                count += 4 * (9 ** remaining)  # First digit can be 1,2,3,4
                return count  # Can't continue with 5 in the number
            else:  # digit < 5
                count += (digit - 1) * (9 ** remaining)  # First digit 1 to (digit-1)
        else:
            # Not first digit - can include 0
            if digit > 5:
                count += 6 * (9 ** remaining)  # 0,1,2,3,4,6
            elif digit == 5:
                count += 5 * (9 ** remaining)  # 0,1,2,3,4
                return count  # Contains 5, stop here
            else:
                count += digit * (9 ** remaining)  # 0 to (digit-1)

        # If we've processed all digits and n doesn't contain 5, include n itself
        if i == length - 1 and '5' not in s:
            count += 1

    print("------------", count)

    return count


def dont_give_me_five(start, end):
    """Count numbers in range [start, end] that don't contain digit 5"""
    if start > end:
        return 0

    # Strategy: use symmetry for negative numbers
    # Count from 1 to abs(n) is same structure as count from -abs(n) to -1

    if start >= 0:
        # Both positive or zero
        return count_up_to(end) - (count_up_to(start - 1) if start > 0 else 0)
    elif end < 0:
        # Both negative: -20 to -10 mirrors 10 to 20
        return count_up_to(-start) - count_up_to(-end - 1)
    else:
        # Spans zero: start < 0 <= end
        negative_count = count_up_to(-start) - 1  # From start to -1 (exclude 0)
        positive_count = count_up_to(end)  # From 0 to end (includes 0)
        return negative_count + positive_count


print(dont_give_me_five(-2490228783604515625, 2490228782196537011))
# print(do_not_give_me_five(-78, 78))
