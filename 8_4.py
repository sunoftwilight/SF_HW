# hw_8_4.py

# 아래 클래스를 수정하시오.
class UserInfo:
    def __init__(self):
        self.user_data = {}
    
    def get_user_info(self):
        try :
            name = input('이름을 입력하세요 : ')
            age = int(input('나이를 입력하세요 : '))
            self.user_data = {
                'name' : name,
                'age' : age
            }

        except ValueError :
            print('나이는 숫자로 입력해야 합니다.')

    def display_user_info(self):
        try :
            print(f"이름 : {self.user_data['name']}")
            print(f"나이 : {self.user_data['age']}")
        except KeyError:
            print('사용자 정보가 입력되지 않았습니다.')

user = UserInfo()
user.get_user_info()
user.display_user_info()
