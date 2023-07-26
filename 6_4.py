# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, val):
    new_dict = dictionary.copy()
    new_dict.setdefault(key, val)
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)   # {'name': 'Alice', 'age': 25, 'country': 'USA'}


# call by reference : 참조값을 넘겨주는 방법
# call by value : 값을 복사하는 방법

# Review of professor
# my_dict['name'] = 'kim'       # 기존의 value 수정
# my_dict['address'] = 'gumi'   # 없던 키이므로 추가
# print(my_dict)                # {'name': 'kim', 'age': 25, 'address': 'gumi'}