# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

def numberOfSteps(num: int)-> int:
    # take the num, check if its even , divide it by 2
    # maintain a count variable.
    # how to check? use modulo, if num % 2 == 0, then its even or else odd.
    # if its odd, then subtract 1 from it.
    # it it turns out to be even or odd, increment count by 1.
    # do this till the num becomes 0 ( repetitive task, so use a loop)
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count+= 1

    return count

print(numberOfSteps(14))
print(numberOfSteps(8))
print(numberOfSteps(123))