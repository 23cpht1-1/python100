# List
# 순서 중요

station_itx = ['용산', '옥수', '왕십리', '청량리', '상봉', '퇴계원', '사릉', '평내호평', '마석', '청평', '가평', '강촌', '남춘천', '춘천']

print(station_itx[0]) # 첫번째
print(station_itx[-2]) # 뒤에서 두번째
# 용산
# 남춘천

# 리스트에 추가
station_itx.append('홍천')

print(station_itx[-1])
# 홍천

# 여러 항목 추가
station_itx.extend(['인제','양구','화천']) # 리스트로 추가

print(station_itx)
# ['용산', '옥수', '왕십리', '청량리', '상봉', '퇴계원', '사릉', '평내호평', '마석', '청평', '가평', '강촌', '남춘천', '춘천', '홍천', '인제', '양구', '화천']

# 총 itx역 수
print(len(station_itx))
# 18

#print(station_itx[18])
# 예외가 발생했습니다. IndexError
# list index out of range
#   File "C:\Users\guaga\Documents\Engineer_Saige\23CP_HT_HJCho\python100\d008_1_list.py", line 27, in <module>
#     print(station_itx[18])
# IndexError: list index out of range

print(station_itx[len(station_itx)-1])
# 화천