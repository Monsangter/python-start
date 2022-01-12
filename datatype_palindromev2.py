def palindrome(a):
    a.lower()
    a.replace(' ', '')

    if a == a[::-1] :
        return True
    else:
        return False

print(palindrome('My gym'))


'''def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]'''