#  num_random_function 교수님 Ver.
import random

#  난수 20개, 1 ~ 20 -> 리스트저장
# myList = []

# for value in range(20):
#     myList.append(random.randint(1,20))

# print(myList)

myList=[13, 16, 3, 10, 3, 2, 13, 12, 15, 14, 8, 16, 3, 15, 3, 9, 18, 17, 5, 8]

min = 21
max = 0
sum = 0
avg = 0.0
#  최소, 최대, 합계, 평균
for value in myList:
    # 최소 - value < min :  value <-min
    if value < min:
        min = value
    # 최대 - value > max :  value <-max
    if value > max:
        max = value
    # 합계
    sum = sum + value
#  평균
avg = sum / len(myList)

print(min,max,sum,avg)
#  중복값, 중복 회수

#  구간 별 히스토그램