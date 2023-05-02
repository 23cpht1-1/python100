import random

i = 100
j = 20e7

# i 이상 j 미만의 아무 숫자 생성
a = random.randrange(i, j)
try:
    b = random.randrange(j, i)
except ValueError:
    print('ValueError on randrange() since start > stop')

# 100 이상 200 이하의 아무 숫자 생성
c = random.randint(100, 200)
try:
    d = random.randint(200, 100)
except ValueError:
    print('ValueError on randint() since 200 > 100')

print('i = ', i, ' and j =', j)
print('randrange() generated number:', a)
print('randint() generated number:', c)

# ValueError on randrange() since start > stop
# ValueError on randint() since 200 > 100
# i =  100  and j = 200000000.0
# randrange() generated number: 166145960
# randint() generated number: 125