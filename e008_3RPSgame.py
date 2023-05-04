# 바위는 0 보는 1 가위는 2
# 각각 그래픽
# 입력값과 랜덤값 비교 -> 승부/무승부

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

img_hands = [rock, paper, scissors]

my_choice = int(input("무엇을 낼까요? 바위(0), 보(1), 가위(2)"))
if my_choice >= 3  or my_choice < 0:
    print("입력이 잘못되었습니다")
else:
    print(f"나의 선택은: {img_hands[my_choice]}")

    com_choice = random.randint(0,2)
    print(f"컴퓨터의 선택은: {img_hands[com_choice]}")

if com_choice == 0 and my_choice == 2:
    print("컴퓨터가 이겼다")
elif my_choice == 0 and com_choice == 2:
    print("내가 이겼다!")
elif com_choice > my_choice:
    print("컴퓨터가 이겼다")
elif my_choice == com_choice:
    print("비겼다")
elif my_choice > com_choice:
    print("내가 이겼다!")

# 무엇을 낼까요? 바위(0), 보(1), 가위(2)2 
# 나의 선택은:
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)

# 컴퓨터의 선택은:
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)

# 내가 이겼다!