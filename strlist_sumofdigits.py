''''''
def sumOfDigits(num):
  #  sum(list(str(num))) unsupported operand types for int and str
    sum = 0
    for c in list(str(num)):
        sum+=int(c)
    return sum
print(list(str(4123)))

print(sumOfDigits(41234))



