# 팁 계산기
# 총 얼마 주문?
# 팁은 몇 %?
# 팁까지 총 얼마?
# 몇 명이서 지불?
# 인당 지불 금액

print("팁 계산기")

order = float(input("총 얼마를 주문했나요?"))
tip = int(input("팁을 몇 %나 줄까요? 10, 12, or, 15 ?"))
people = int(input("몇 명이서 나눠 내나요?"))

tip_as_percent = tip / 100
total_tip = order * tip_as_percent
total_bill = total_tip + order
bill_per_person = total_bill / people

# 소수점 둘째자리까지
final_bill = round(bill_per_person, 2)
print(f"팁을 포함해 각자가 낼 금액은: {final_bill}$입니당")
