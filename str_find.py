s = 'hello Python!'
#s.find('P')는 P의 인덱스를 반환한다.

h = s[0:s.find('P')]
print(h.rstrip())
#rstrip 하면 공복 벗겨짐.
print(s[0:s.find('P')-1])
