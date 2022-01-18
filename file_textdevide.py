text = open('/Users/monsangter/PycharmProjects/python-start/postcard.txt', 'r').read()
print(text + '\n')

head,body,tail = text.split('\n\n')
print(body + '\n')

import re

body2 = re.sub('[:,/.]', '', body)
print(body2 + '\n')

print(body2.upper())

secretwords=[]
for line in body2.split('\n'):
    secretwords += line.split()[:2]

message = ' '.join(secretwords)

print(message)