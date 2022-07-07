# 랜덤 함수
# -> 난수 발생기

import random

# 0이상 1미만의 실수를 반환
# 0.0 ~ 0.9999999999......
for value in range(10):
    print(int(random.random()* 3)+1)