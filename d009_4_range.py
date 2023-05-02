# 반복수행으로 일정 범위의 숫자 출력
a = 1; b = 10
for num in range(a, b):
    print(num)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for num in range(1, 11, 3): # 1 이상 11 미만을 3 간격으로
    print(num)
# 1
# 4
# 7
# 10

# 1~100 다 더하기
total = 0
for num in range(1,101):
    total += num
print(total)
# 5050

# 짝수 더하기
total = 0
'''
for num in range(1, 101, 2):
    print(num)
# 이 경우 홀수 나열
'''
for num in range(2, 101, 2):
    total += num
print(total)
# 2550

# 짝수 더하기2
total = 0
for num in range(1, 101):
    if num % 2 == 0:
        total += num
print(total)
# 2550