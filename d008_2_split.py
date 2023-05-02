# split string method
import random

name_friend = input('대장 후보 이름을 쉼표로 구분해서 입력하세요: ')
names = name_friend.split(',')

print(names)

# 가족 구성원의 이름을 쉼표로 구분해서 입력하세요: 원일, 후순, 세희, 세영
# ['원일', ' 후순', ' 세희', ' 세영']

# 리스트의 요소 개수
num_member = len(names)

# 랜덤으로 인덱스 선택
random_choice = random.randint(0, num_member - 1)

chosen_mem = names[random_choice]
print(chosen_mem + '(이)가 오늘 대장임')

# 대장 후보 이름을 쉼표로 구분해서 입력하세요: 세희, 미선, 유진
# ['세희', ' 미선', ' 유진']
#  유진(이)가 오늘 대장임