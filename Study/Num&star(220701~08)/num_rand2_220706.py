import random

# 0 ~ 5 정수 랜덤값
for value in range(10):
    num = int(random.random()*5)
    print(num)

print("----------------------------")

# -5 ~ 5 정수 랜덤값
for value in range(50):
    num = int(random.random()*11)-5
    print(num)