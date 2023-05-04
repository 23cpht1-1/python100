# 최고점수 구하기
# 78 65 89 86 55 91 64 89

student_scores = input('점수를 띄어쓰기로 구분하여 입력하셈: ').split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# print(max(student_scores))
# max()나 min() 함수로 간단히 표현 가능하지만 for문으로 시도해보자

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f'최고점: {highest_score}')

# 점수를 띄어쓰기로 구분하여 입력하셈: 78 65 89 86 55 91 64 89
# [78, 65, 89, 86, 55, 91, 64, 89]
# 최고점: 91