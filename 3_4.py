# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3
result = abs(negative)
print(result)

# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []
print(bool(empty_list))   # 0, '', [], {} 는 False
# boolean 판단 : bool()

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
my_list = [1, 2, 3, 4, 5]
# len_list = len(my_list)
# sum_list = 0
# for i in range(len_list):
#     sum_list += my_list[i]
# print(sum_list)
print(sum(my_list))    # sum 함수를 이용하면 한번에 더하기 가능

# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
sorted_list = sorted(unsorted_list)        # 비파괴 함수 (원본 변경 X, 반환값만 변경)
print(sorted_list)
# sorted : 오름차순 정렬

# unsorted_list.sort()      # 파괴 메서드 (원본 자체를 변경)
# print(unsorted_list)