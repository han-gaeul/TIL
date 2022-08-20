#### `클래스`

---------------

- 클래스 속성(attribute)

  - 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성

  - 클래스 선언 내부에서 정의

  - classname.name으로 접근 및 할당

    ```python
    class Circle:
      pi = 3.14 # 클래스 변수 정의
      
    c1 = Circle()
    c2 = Circle()
    
    print(Circle.pi)
    print(c1.pi)
    print(c2.pi)
    ```

    >3.14
    >
    >3.14
    >
    >3.14

- 인스턴스와 클래스 간의 이름 공간(namespqce)

  - 클래스를 정의하면 클래스와 해당하는 이름 공간 생성
  - 인스턴스를 만들면 인스턴스 객체가 생성되고 이름 공간 생성
  - 인스턴스에서 특정 속성에 접근하면 인스턴스-클래스 순으로 탐색

- 클래스 메소드

  - 클래스가 사용할 메소드

  - `@classmethod` 데코레이터를 사용하여 정의

    - 데코레이터 : 함수를 어떤 함수로 꾸며서 새로운 기능을 부여

  - 호출 시, 첫번째 인자로 클래스(cls)가 전달 됨

    ```python
    class MyClass
    	
      @classmethod
      def class_method(cls, arg1, ...)
    ```

    > MyClass.class_mehod(...)

- 스태틱 메소드

  - 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

- 언제 사용?

  - 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때 사용
  - `@staticmethod` 데코레이터를 사용하여 정의
  - 호출 시, **어떠한 인자도 전달되지 않음** (클래스 정보에 접근/수정 불가)

#### 📝 클래스 정리

- 클래스 구현
  - 클래스 정의
  - 데이터 속성 정의 (객체의 정보는 무엇인지)
  - 메소드 정의 (객체를 어떻게 사용할 것인지)
- 클래스 활용
  - 해당 객체 타입의 인스턴스 생성 및 조작



#### 📝 메소드 정리

- 인스턴스 메소드

  - 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작

- 클래스 메소드

  - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작

- 스태틱 메소드

  - 인스턴스나 클래스를 의미하는 매개변수는 사용하지 않음

    ✔︎ 즉, 객체 상태나 클래스 상태를 수정할 수 없음

  - 일반 함수처럼 동작하지만 클래스의 이름공간에 귀속 됨

    ✔︎ 주로 해당 클래스로 한정하는 용도로 사용

- 예시

```python
class MyClass:
  
  def method(self):
    return 'instance method', self
  
  @classmethod
  def classmethod(cls):
    return 'class method', cls
  
  @staticmethod
  def staticmethod():
    return 'static method'
```



#### 🔎 객체지향의 핵심 4가지

##### `추상화`

```python
# 학생(Student)을 표현하기 위한 클래스를 생성합니다.
class Student:
  
  def __init__(self, name, age, qpa):
    self.name = name
    self.age = age
    self.qpa = qpa
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
    
  def study(self):
    self.qpa += 0.1
```

```python
# 교수(Professor)를 표현하기 위한 클래스를 생성합니다.

class Student:
  
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.separtment = department
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
    
  def teach(self):
    self.age += 1
```

```python
class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def talk(self):
    print(f'반갑습니다. {self.name}입니다.')
```



##### `상속`

- 두 클래스 사이 `부모 - 자식 관계`를 정립하는 것

- 클래스는 상속이 가능함

  - 모든 파이썬 클래스는 object를 상속 받음

  ```python
  class ChildClass(ParentClass):
    pass
  ```

- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음

- 부모 클래스의 속성, 메소드가 자식 클래스에 상속되므로 코드 재사용성⬆︎

- 상속을 통한 메소드 재사용

  ☑️ In [1] :

  ```python
  class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def talk(self):
      print(f'반갑습니다. {self.name}입니다.')
      
  class Professor(Person):
    def __init__(self, name, age, department):
      self.name = name
      self.age = age
      self.department = department
      
  class Student(Person):
    def __init__(self, name, age, qpa):
      self.name = name
      self.age = age
      self.qpa = qpa
  ```

  ☑️ In [2] :

  ```python
  p1 = Professor('김교수', 49, '컴퓨터공학과')
  ```

  ☑️ In [3] :

  ```python
  s1 = Student('김학생', 20, 3.5)
  ```

  ☑️ In [4] :

  ```python
  # 부모 Person 클래스의 talk 메서드를 활용
  p1.talk()
  ```

  > 반갑습니다. 김교수입니다.

  ☑️ In [5] :

  ```python
  s1.talk()
  ```

  > 반갑습니다. 김학생입니다.

- 상속 관련 함수와 메소드
  - Isinstance *(object, classinfo)*
    - classinfo의 instance거나 subclass인 경우 True