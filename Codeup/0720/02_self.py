class Person:

    # 사람이라면 이름을 가지고 있다.
    # 인스턴스를 만들 때는 이름 정보를 받고 싶다.
    # 생성자 메서드
    # 함수의 문법과 동일
    def __init__(self, name):
        # 개별 인스턴스에 각각 name 속성을 지정
        self.name = name

    # self : 호출하는 인스턴스를 파이썬 내부적으로 전달해줌
    # wendy.greeting() 이렇게 호출 되면
    # 이런 느낌처럼 Person.greeting(wendy)
    def greeting(self):
        # print('안녕하세요. 땡떙입니다.')
        # 개별 인스턴스의 속성으로 쓰고 싶다.
        # 함수에서 우리가 어떠한 값을 쓰려면 해야하는 일은? 파라미터로 넘겨준다.
        print(f'안녕하세요, {self.name}입니다.')

# 인스턴스 만들 때
wendy = Person('웬디')
wendy.greeting()
# Person.greeting(wendy)

tang = Person('땡떙')
tang.greeting()

# 인스턴스 메서드 중에 첫번째로 self를 넘겨준다 하는 약속이 되어있음
# 내부적으로 호출 될 때는 다른 모습이 있다
# self라는게 각 인스턴스의 