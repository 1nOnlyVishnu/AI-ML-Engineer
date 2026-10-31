# Reverser_interger

1.  convert the integer into a string because reversing a string is
    pretty ez in Python.
2.  then check whether the number is negative, and if it is, temporarily
    remove the negative sign.
3.  then reverse the string using slicing, convert it back into an
    integer, and restore the negative sign.
4.  Finally check whether the reversed number falls within the allowed
    32 bit integer range. If it doesn't return 0.
5.  Downside of this approach is it USES EXTRA SPACE.

``` python
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
```

# Palindrome_number

1.  Make use of Two pointer approach.
2.  Convert the number into a string
3.  one pointer ( left ) at 0th index and other one ( right ) at the
    last index
4.  compare characters from each end, if they are not equal return
    False, if they are equal increment left pointer by 1 index and
    decrement right pointer by 1. Keep doing this until the whole string
    is processed.(use a while loop). If the pointers cross each other,
    it means the whole string is processed, so outside the loop return
    True.

``` python
class Solution:

def isPalindrome(x:int)-> bool:

    st = str(x)
    i = 0
    j = len(st) - 1
    while i < j:
        if st[i] != st[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
```

# Count the Digits That Divide a Number

1.  The idea is to take one digit from the given number and check
    whether it divides the given number completely ( remainder should be
    0).
2.  To extract one digit at a time, use modulo operator with the number
    10.
3.  use this digit to see if it completely divides the original given
    number, if it does , then keep track of the count. (Maintain a
    variable called Count)
4.  then after processing , remove this last digit by dividing it by
    10.( use integer division in python "//" )
5.  keep doing this until the given number becomes 0.

``` python
def countDigits(self, num: int) -> int:
    original_num = num
    count = 0
    while num > 0:
        last_digit = num % 10
        if original_num % last_digit == 0:
            count += 1
         num = num // 10

    return count
```
