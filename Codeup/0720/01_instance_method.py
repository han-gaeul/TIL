class Person:
    # 클래스 변수(속성)
    species = '사람'

    # 인스턴스 메서드
    # 인스턴스가 활용 할 메서드
    def greeting(self):
        print('안녕')

wendy = Person()
wendy.greeting() # 메서드 호출

# 클래스 변수(속성)
print(Person.species) # 변수이기 때문에 호출X