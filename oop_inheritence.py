class Person:
    eyes = 2
    nose = 1
    mouth = 1
    ears = 2
    arms = 2
    legs = 2

    def eat(self):
        print('얌냠...')

    def sleep(self):
        print('쿨쿨...')

    def talk(self):
        print('주절주절')

class Student(Person):
    def study(self):
        print('열공열공...')


lee = Person()
print(lee.mouth)
print(lee.talk())
kim = Student()
print(kim.mouth)
print(kim.talk())

print(kim.study())