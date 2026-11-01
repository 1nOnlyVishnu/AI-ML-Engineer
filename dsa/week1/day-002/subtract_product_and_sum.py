# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

# Example 1:

# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

def subtractProductAndSum(n:int)->int:
    product = 1 # dont initialize with 0 cuz anything multiplied by 0 gives you 0.
    digit_sum = 0
    
    while n > 0:
        last_digit = n % 10 # extract one digit at a time using modulo op with 10
        product = product * last_digit
        digit_sum = digit_sum + last_digit
        n = n // 10 # remove the last_digit from the number "n". we dont want to process the same number again and again. Use integer division "//"
    return product - digit_sum

print(subtractProductAndSum(234))
print(subtractProductAndSum(4421))


