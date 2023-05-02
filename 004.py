# 퀴즈 4-1)

# 1. 잘못된 설명은 무엇일까요?
# - a. 932는 정수다.
# - b. "false"는 부울값이다 -> 큰 따옴표 안에 있으니까 문자열!
# - c. 857.25 는 실수다
# - d. "523"은 문자열이다

# 2. 변수 mystery의 데이터 형식은 무엇일까요? 

mystery = 734_529.678

# - a. 정수
# - b. 문자열
# - c. 부울값
# - d. 실수 -> 소수점이 붙은 값은 실수

# 3. 다음 코드로 출력하게 될 값은? 

#street_name = "동산면 영서로 1290-31"
#print(Street_name[4] + Street_name[9])
# 예외가 발생했습니다. NameError
# name 'Street_name' is not defined
#   File "C:\Users\guaga\Documents\Engineer_Saige\23CP_HT_HJCho\python100\004_1.py", line 35, in <module>
#     print(Street_name[4] + Street_name[9])
# NameError: name 'Street_name' is not defined

street_name = "동산면 영서로 1290-31"
print(street_name[4] + street_name[9])
# 영2
## 5번째 글자, 10번째 글자

# 퀴즈 4-2)

# 4. 2자리의 숫자를 입력받아 앞자리와 뒷자리의 값을 더하세요.
num = input("2자리 수 입력:")
plus = int(num[0]) + int(num[1])
print("각 자리의 합은 "+ str(plus))
# 2자리 수 입력:92
# 각 자리의 합은 11
