# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하나요?
# 정의할 때 이름을 지어놓고 호출 할 때 값을 넘겨줘요

class MyClass:
    # 클래스 차원에서 쓸 수 있는 변수
    class_variable = '클래스 변수'

    # 메서드를 정의함
    def __init__(self):
        self.instance_variable = '인스턴스 변수'

    # 인스턴스 메서드 정의
    def instance_method(self):
        return self, self.instance_variable

    # 클래스 메서드 정의
    @classmethod
    def class_method(cls):
        return cls, cls.class_variable

    # 스태틱 메서드 정의
    @staticmethod # @ 데코레이터 : 함수를 꾸며주는 것. 지금은 안 봐도..
    def static_method():
        return '스태틱'

c1 = MyClass()

print('인스턴스 변수 호출', c1.instance_variable)
print('인스턴스 메서드 호출', c1.instance_method())
print('클래스 메서드 호출', c1.class_method())
print('스태틱 메서드 호출', c1.static_method())

# 출력
# 인스턴스 변수 호출 인스턴스 변수
# 인스턴스 메서드 호출 (<__main__.MyClass object at 0x10506ba00>, '인스턴스 변수')
# 클래스 메서드 호출 (<class '__main__.MyClass'>, '클래스 변수')
# 스태틱 메서드 호출 스태틱


# self, cls는 관용적 표현(이름 붙이기). 변경 가능
# 스태틱 메서드 안에서 클래스, 인스턴스를 사용할 수 없다