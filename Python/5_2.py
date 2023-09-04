# main.py

# 아래 함수를 수정하시오.
def count_character(string, obj):
    N = list(string).count(obj)
    return N

# solve with for & if
def count_character2(string, obj):
    count = 0
    for chars in string:
        if chars == obj:
            count += 1
    return count

result = count_character("Hello, World!", "o")
print(result) # 2

result2 = count_character2("Hello, World!", "o")
print(result2) # 2
