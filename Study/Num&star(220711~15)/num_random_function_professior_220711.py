#  num_random_function 교수님 Ver.
import random

#  난수 20개, 1 ~ 20 -> 리스트저장
myList = []

for value in range(20):
    myList.append(random.randint(1,20))

print(myList)

#  최소, 최대, 합계, 평균
#  중복값, 중복 회수
#  구간 별 히스토그램