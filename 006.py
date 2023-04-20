# BMI지수로 저체중, 정상, 과체중, 비만 표시하기

print("BMI 측정기입니다")
height = int(input("키(cm)를 입력해주세요: "))
weight = int(input("몸무게(kg)를 입력해주세요: "))

BMI = weight / (height/100)**2
BMI_round = round(BMI,1)

if BMI > 30.0:
    print(f"BMI지수는 {BMI_round}(으)로, 비만에 해당합니다.")
elif BMI >= 25.0:
    print(f"BMI지수는 {BMI_round}(으)로, 과체중에 해당합니다.")
elif BMI >= 18.5:
    print(f"BMI지수는 {BMI_round}(으)로, 정상에 해당합니다")
else:
    print(f"BMI지수는 {BMI_round}(으)로, 저체중에 해당합니다")