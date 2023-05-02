#파이썬 피자에 오신 것을 환영합니다!
#피자 사이즈는 S, M, L
#S는 15000, M은 20000, L은 30000원
#페퍼로니 추가는 2000원
#치즈 추가는 3천원
#총 지불액

print("피자주문 ㄱㄱ")
size = input('사이즈 선택 s/m/l').lower()
bill = 0

if size == 's':
    bill = 15000
    print(f'선택 사이는 {size}, 가격은 {bill}원')
elif size == 'm':
    bill = 20000
    print(f'선택 사이는 {size}, 가격은 {bill}원')
elif size == 'l':
    bill = 30000
    print(f'선택 사이는 {size}, 가격은 {bill}원')
else:
    print('잘못된 선택. 프로그램 종료 후 재실행 부탁')

pep = input('페퍼로니 추가? y/n ').lower()
if pep == 'y':
    bill += 2000
    print('페퍼로니 추가됨')

cheese = input('치즈 추가? y/n ').lower()
if cheese == 'y':
    bill += 3000
    print('치즈 추가됨')

print(f'지불총액 {bill}원')

# 피자주문 ㄱㄱ
# 사이즈 선택 s/m/ls
# 선택 사이는 s, 가격은 15000원
# 페퍼로니 추가? y/n y
# 페퍼로니 추가됨
# 치즈 추가? y/n n
# 지불총액 17000원