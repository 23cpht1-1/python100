# 4-5 파이썬의 숫자처리 및 F-string

print(int(8/3))
# 2

print(round(8/3))
print(round(8/3, 2))
print(round(0.145676747234, 2))
# 3
# 2.67
# 0.15

print(8//3)
# 2
## 소수점 뒤 버림

score = 0
score += 1
print(score)
# 1

score = 0
height = 1.8
earth = True

print(f"당신의 스코어는 {score}, 당신의 키는 {height}, 당신은 지구인입니다.{earth}")
# 당신의 스코어는 0, 당신의 키는 1.8, 당신은 지구인입니다.True
