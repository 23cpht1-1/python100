# 4-4 BMI 계산기

height = input("당신의 키(m): ")
weight = input("당신의 몸무게(kg): ")

bmi = int(weight) / float(height)**2
bmi_as_int = int(bmi)

print(bmi_as_int)

# 당신의 키(m): 1.83
# 당신의 몸무게(kg): 79
# 23