# 키 리스트 = [180,154,165,173,180,169,146]
# 평균 구하는 데 for문 사용
# 모두의 키를 더하고, 학생수로 나누고, 정수로 반올림

# # 1번째 방법
# student_heights = input('학생들의 키를 띄어쓰기로 구분하여 입력쓰: ').split()   # () 안에 아무것도 안 넣으면 스페이스로 구분
# student_num = len(student_heights)
# print(student_num)

# for n in range(0, len(student_heights)):    # range(n,m)은 n 이상 m 미만이니까!
#     student_heights[n] = int(student_heights[n])

# height_avg = sum(student_heights) / student_num

# print(round(height_avg))

# # 학생들의 키를 띄어쓰기로 구분하여 입력쓰: 180 154 165 173 180 169 146
# # 7
# # 167

# # 2번째 방법
# student_heights = input('학생들의 키를 띄어쓰기로 구분하여 입력쓰: ').split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)

# total_height = 0
# for height in student_heights:
#     total_height += height
# print(total_height)

# num_of_students = len(student_heights)
# height_avg = round(total_height / num_of_students)
# print(height_avg)

# # 학생들의 키를 띄어쓰기로 구분하여 입력쓰: 180 154 165 173 180 169 146
# # [180, 154, 165, 173, 180, 169, 146]
# # 1167
# # 167

# 3번째 방법
student_heights = input('학생들의 키를 띄어쓰기로 구분하여 입력쓰: ').split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

num_of_students = 0
for student in student_heights:
    num_of_students += 1
print(num_of_students)

height_avg = round(total_height / num_of_students)
print(height_avg)

# 학생들의 키를 띄어쓰기로 구분하여 입력쓰: 180 154 165 173 180 169 146
# [180, 154, 165, 173, 180, 169, 146]
# 1167
# 7
# 167