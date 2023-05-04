print("파이썬 피자에 오신 것을 환영합니다!")
size = input("원하는 사이즈는 무엇인가요? S, M, L 중 골라주세요!")
bill = 0

if size.lower() == "s":
    bill = 15000
    print(f"S 사이즈는 {bill}원입니다.")
elif size.lower() == "m":
    bill = 20000
    print(f"M 사이즈는 {bill}원입니다.")
elif size.lower() == "l":
    bill = 30000
    print(f"L 사이즈는 {bill}원입니다.")
else:
    print("잘못된 사이즈를 입력하셨습니다. 프로그램을 종료한 후 다시 시도해주세요!")
    # 프로그램 종료 코드 필요

topping = input("토핑을 추가하시겠습니까? y/n")
if topping.lower() == 'y':
    pepperoni = input("페퍼로니를 추가하시겠습니까? y/n")
    if pepperoni.lower() == 'y':
        bill += 2000
    cheese = input("치즈를 추가하시겠습니까? y/n")
    if cheese.lower() == 'y':
        bill += 3000

print(f"주문을 종료합니다\n 지불하실 총 금액은 {bill}원입니다\n 이용해주셔서 감사합니다")

# 파이썬 피자에 오신 것을 환영합니다!
# 원하는 사이즈는 무엇인가요? S, M, L 중 골라주세요!l
# L 사이즈는 30000원입니다.
# 토핑을 추가하시겠습니까? y/ny
# 페퍼로니를 추가하시겠습니까? y/nn
# 치즈를 추가하시겠습니까? y/ny
# 주문을 종료합니다
#  지불하실 총 금액은 33000원입니다
#  이용해주셔서 감사합니다