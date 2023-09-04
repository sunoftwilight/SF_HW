# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        try :
            name = input('이름을 입력하세요 : ')           # name과 age는 함수 안에서 쓰고 버릴 지역변수 -> self 붙여 인스턴스 만들 필요 X (어차피 딕셔너리에 넣기만 하면 끝날 자료임)
            age = int(input('나이를 입력하세요 : '))
            self.user_data = {
                'name' : name,
                'age' : age
            }

        except ValueError :
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        try :
            print(f"사용자 정보 : \n이름 : {self.user_data['name']}")
            print(f"나이 : {self.user_data['age']}")

            # name = self.user_data['name']        먼저 name, age를 할당받으면 사용자 정보를 분리해서 작성할 수 있음
            # age = self.user_data['age']
            # print('사용자 정보: ')
            # print('이름: ', name)
            # print('나이: ', age)

        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
