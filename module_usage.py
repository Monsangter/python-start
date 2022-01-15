import calendar
print(dir(calendar))
a = [x for x in dir(calendar) if 'leap' in x]#list comprehension
print(a)

help(calendar.isleap)
help(calendar.leapdays)

print(calendar.isleap(2077))