import random

lotto1 = random.randint(1,46)
lotto2 = random.randint(1,46)
if lotto2 == lotto1:
    lotto2 = random.randint(1,46)
lotto3 = random.randint(1,46)
if lotto3 == lotto2 or lotto1:
    lotto3 = random.randint(1,46)
lotto4 = random.randint(1,46)
if lotto4 == lotto2 or lotto1 or lotto3 :
    lotto4 = random.randint(1,46)
lotto5 = random.randint(1,46)
if lotto5 == lotto2 or lotto1 or lotto3 or lotto4 :
    lotto5 = random.randint(1,46)
lotto6 = random.randint(1,46)
if lotto6 == lotto2 or lotto1 or lotto3 or lotto4 or lotto5 :
    lotto6 = random.randint(1,46)
# 제대로 하려면 반복문을 써야 할 각

print(f"{lotto1}    {lotto2}    {lotto3}    {lotto4}    {lotto5}    {lotto6}")
# 1    14    31    5    4    6    


    
