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

print(isPalindrome(-121))

