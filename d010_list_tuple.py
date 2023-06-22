list1 = [0, 1,2,3,4,5, 6, 7, 'a', 'b']
# print(type(list1), list1)

###########
# print(list1[1], list1[7])
# print(list1[2:5]) # 5번 '미만' (slicing 2~5라는 뜻)
# print(list1[:7]) # 처음부터 7개
# print(list1[4:]) # 4번부터 끝까지
# print(list1[-1]) # -가 붙으면 거꾸로
# print(list1[-4:]) # 뒤에서부터 4개
# print(list1[1+2:]) # 연산도 가능

#############
# list1[6] = 'c' # 그 자리가 대체됨
# print(list1)

# 인덱스 범위를 벗어난 리스트를 불러오면 오류남 -> len()으로 길이 파악

##############
list2 = [] # element가 없는 빈 리스트도 만들 수 있음

for item in range (11, 14, 1):
    list2 += [item]
    #list2.append(item) 해도 동일한 결과

# print(list2)   
# #----[11, 12, 13]

####################
# list3 = []
# list3 += 'Python'
# print(list3, len(list3))
# #--- ['P', 'y', 't', 'h', 'o', 'n'] 6

# # tuple은 ()로 묶음 -> 내용 수정 불가능
# list3 += ('S', 't', 'u', 'd' ,'y')
# print(list3, len(list3))
# #--- ['P', 'y', 't', 'h', 'o', 'n', 'S', 't', 'u', 'd', 'y'] 11

# ###############
# list12 = list1 + list2
# print(list12)
# #--- [0, 1, 2, 3, 4, 5, 6, 7, 'a', 'b', 11, 12, 13]

# # 인덱스와 엘리먼드 동시에 찍기 -> 인덱스와 리스트 요소를 개별적으로 매칭
# for i in range(len(list12)):
#     print(f'({i}, {list12[i]})', end = ' ')
# #--- (0, 0) (1, 1) (2, 2) (3, 3) (4, 4) (5, 5) (6, 6) (7, 7) (8, a) (9, b) (10, 11) (11, 12) (12, 13)

#######
# # tuple 예시
# t1 = 10, 20, 30, 'John'
# t1 += (40, 50) # 기존 튜플에 요소 덧붙이기
# print(t1)
# #--- (10, 20, 30, 'John', 40, 50)

# #####
# t3 = 'A', 'B', 'C', '[90,80,70]' # 괄호(){}[]로 안 묶으면 tuple로 인식함
# print(t3, len(t3), t3[3])
# #--- ('A', 'B', 'C', '[90,80,70]') 4 [90,80,70]

###########
# 언패킹(구성요소들을 따로 뽑아내고 변수로 할당)
t4 = (('A', 'B', 'C'), [90,80,70])
print(len(t4))
#--- 2
grade, number = t4 # 등급, 점수를 변수로 할당함
print(grade, number, type(grade), type(number))
#--- ('A', 'B', 'C') [90, 80, 70] <class 'tuple'> <class 'list'>

# 파이썬에서 모든 시퀀스(배열)은 언패킹할 수 있음!
num1, num2, num3 = number
print(num1, num2, num3)
#--- 90 80 70

# 문자열도 언패킹
first, second, third, fourth = 'WIFI'
print(first, second, third, fourth)
#--- W I F I