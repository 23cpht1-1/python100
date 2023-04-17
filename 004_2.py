# 4-2 데이터 형식과 함수

num_char = len(input("당신의 이름은 무엇입니까?"))
print(type(num_char))
# 당신의 이름은 무엇입니까?권세희
# <class 'int'>
## ???? 내 이름이 정수네????? 모징 아 아니다 len()때문이구낰ㅋㅋ

num_char = input("당신의 이름은 무엇입니까?")
print(type(num_char))
# 당신의 이름은 무엇입니까?권세희
# <class 'str'>

num_char = len(input("당신의 이름은 무엇입니까?"))
new_num_char = str(num_char)
print("내 이름은" + new_num_char + "글자짜리당")
# 당신의 이름은 무엇입니까?권세희
# 내 이름은3글자짜리당

a = 123
print(type(a))
# <class 'int'>

a = str(123)
print(type(a))
# <class 'str'>

a = float(123)
print(type(a))
# <class 'float'>