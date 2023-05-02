#롤러코스터를 타면서 사진도 찍을 것인가?
print("롤코 환잉환잉")
height = int(input("키 몇 cm?"))
bill = 0

if height >= 120:
    print("롤코 탑승 가넝")
    age = int(input("몇 살?"))
    if age < 12:
        bill = 0
        print('무료')
    elif age <= 18:
        bill = 7000
        print('청소년 7000원')
    else:
        bill = 12000
        print('성인 12000원')

    wants_photo = input('사진? y/n')
    if wants_photo == 'y':
    # 천원 추가
        bill += 1000
        print(f'지불총액 {bill}')

else:
    print('탑승불가')

# 롤코 환잉환잉
# 키 몇 cm?199
# 롤코 탑승 가넝
# 몇 살?78
# 성인 12000원
# 사진? y/ny
# 지불총액 13000