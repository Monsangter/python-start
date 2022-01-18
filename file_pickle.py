users = {'kim':'3kid9', 'sun80':'393948', 'ljm':'py90390'}
f = open('users', 'wb')
#필요한 로우데이타가 있을때 미리 필요한 부분을 딕셔너리, 리스트, 튜플등의 자료구조로 저장해놓게되는데
#문자열이 아닌 객체를 파일에 쓸 수 없기에 pickle모듈을 활용해 그 객체 자체를 바이너리로 저장한다.
import pickle

pickle.dump(users, f)
f.close()

f = open('users', 'rb')
a = pickle.load(f)
print(a)