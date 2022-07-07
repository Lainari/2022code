# 랜덤함수를 사용하기위해 랜덤함수 모듈 import <- 필수
import random

# 0 ~ N 실수 랜덤값
for value in range(10):
    num = random.random()*10 # 랜덤함수인 random.random() 과 0 ~ N 까지 범위를 정해주는 *N
    print(num)
print()
print("------------------------")
print()
# 0 ~ N 정수 랜덤값
for value in range(10):
    num = int(random.random()*10)
    print(num)