def reverse(self, x: int) -> int:
    sign = -1 if x < 0 else 1

    x = abs(x)

    reversed_num = int(str(x)[::-1])

    reversed_num *= sign

    MIN = -2147483648
    MAX = 2147483647

    if reversed_num < MIN or reversed_num > MAX:
        return 0

    return reversed_num

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



# NEETCODE'S CODE.
def reverse_integer(x: int)-> int:
    MIN = -2147483648
    MAX = 2147483647

    res = 0
    sign = -1 if x < 0 else 1

    x = abs(x)

    while x > 0:
        digit = x % 10
        x //= 10

        if res > MAX // 10 or (res == MAX // 10 and digit > 7):
            return 0

        res = res * 10 + digit

    res *= sign

    if res < MIN or res > MAX:
        return 0

    return res

print(reverse_integer(-123))


