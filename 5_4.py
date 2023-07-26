# main.py

# 아래 함수를 수정하시오.
def find_min_max(num_list):
    i = len(num_list) - 1
    num_list.sort()
    return (num_list[0], num_list[i])

result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)


# solve with for & if
def find_min_max2(num_list):
    min = num_list[0]
    max = num_list[0]
    for num in num_list:
        if num < min:
            min = num
        if num > max :
            max = num
    return (min, max)

result2 = find_min_max2([3, 1, 7, 2, 5])
print(result2)


# review of professor
# 2차원 배열의 최대/최소값 구할 경우에는 첫번째 인덱스 값을 초기값으로 설정할 수 없으므로 최대한 작은수 / 큰 수로 설정하는 방법을 사용할 것
def find_min_max3(lst):
    # 초기값 설정
    min_v = 987654321
    max_v = 0           
    #lst에 양수만 속했을 경우이므로 0 설정  
    # (음수 포함이면 -987654321 등 매우 작은수로 설정하기)

    # min_v = max_v = lst[0] 로도 사용 가능

    for num in lst:
        if min_v > num :
            min_v = num
        if max_v < num :
            max_v = num
    return min_v, max_v     # (min_v, max_v) 와 동일한 출력

result3 = find_min_max3([3, 1, 7, 2, 5])
print(result3)


# +) len 함수를 쓰지 못할 경우 for문을 통해 길이 구하기 가능
def length_list(lst):
    cnt = 0
    for num in lst:
        cnt += 1
    return cnt

result4 = length_list([3, 1, 7, 2, 5])
print(result4)   # 5


# +) sum 함수를 쓰지 못할 경우 for문을 통해 합 구하기 가능
def sum_list(lst):
    sum_lst = 0
    for num in lst:
        sum_lst += num
    return sum_lst

result5 = sum_list([3, 1, 7, 2, 5])
print(result5)   # 18

