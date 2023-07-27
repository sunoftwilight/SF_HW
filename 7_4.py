# hw_7_4.py

# 아래 클래스를 수정하시오.
class Person:
   number_of_people = 0                # 클래스 변수

   def __init__(self, name, age):      # 생성자 메소드 역시 인스턴스 메서드의 일종
      self.name = name                 # self.name => 인스턴스 변수
      self.age = age                   # 인스턴스 변수
      Person.number_of_people += 1     # self로 써도 실행은 됨 (자신한테 없으면 상위로 올라가서 찾으니까) 다만 권장하지 않는 방법임.

   
   def introduce(self):
      print(f'제 이름은 {self.name}이고, 저는 {self.age}살 입니다.')

person1 = Person("Alice", 25)        # Person("Alice", 25) 를 실행하면 Alice & 25 속성을 가진 메모리 생성 -> 이게 "인스턴스" -> 이 인스턴스를 person1이라는 이름에 할당하면 "객체" 
                                     # 따라서 person1은 객체이자 Person의 인스턴스
person1.introduce()
print(Person.number_of_people)