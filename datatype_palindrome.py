def palindrome(a):

    if a == a[::-1] :
        return True
    else:
        return False

print(palindrome('na'))

#슬라이싱은 문자열에 대한 것.