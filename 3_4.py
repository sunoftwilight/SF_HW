# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
result = abs(negative)
print(result)

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(bool(empty_list))
# boolean 판단 : bool()

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
len_list = len(my_list)
sum_list = 0
for i in range(len_list):
    sum_list += my_list[i]
    
print(sum_list)

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
sorted_list = sorted(unsorted_list)
print(sorted_list)
# sorted : 오름차순 정렬