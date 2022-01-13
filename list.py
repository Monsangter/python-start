prime = [3 , 7, 11]
prime.append(5)
print(prime)
prime.sort()
print(prime)
prime.insert(0, 2)#인덱스 0 에 2를 삽입
print(prime)
del prime[4]#번호
print(prime)
a = prime.pop()
print(prime, a)
#맨 뒤 원소를 pop 하고 a에 초기화!

prime[0] = 1
print(prime)
#인덱스로 바로 insert가능
orders = ['potato', ['pizza', 'Coke', 'salad'], 'hamburger']
print(orders[1])
print(orders[1][2])

matrix=[[1,2,3], [4,5,6], [7,8,9]]
