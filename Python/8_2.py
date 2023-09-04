# hw_8_2.py

# 아래 함수를 수정하시오.
def check_number():

    try :
        num = int(input('숫자를 입력하세요: '))  
        # 해당 input을 받는 과정에서 숫자가 아닌 것을 입력하는 등 "예외가 발생"할 수 있으므로, try 안에서 받아와야함!! try문 밖에서 적으면 예외 발생 코드가 try 밖에 있으므로 except에서 인식 못함

        if num > 0 :
            print('양수입니다.')
        elif num < 0 :
            print('음수입니다.')
        else :
            print('0입니다.')

    except ValueError :
        print('잘못된 입력입니다.')

check_number()