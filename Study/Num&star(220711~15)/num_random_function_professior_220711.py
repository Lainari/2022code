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

temp=[]
duplicatedNum = [0] * len(myList) # 같은 원소를 len(myList) 개수만큼 생성

#  중복값, 중복 회수
for value in myList:
    # value in temp -> 중복값
    # duplicatedNum[value - 1] 1 증가
    if value in temp:
        duplicatedNum[value - 1] += 1
    else:
    # else 신규값
    # temp에 신규 값 추가
        temp.append(value)
index = 1
for value in duplicatedNum:
    if value >= 1:
        print(index, value + 1)

    index += 1
#  구간 별 히스토그램
numForInterval = [0]*4

for value in myList:
    if 1 <= value <= 5:
        numForInterval[0] += 1
    elif 6 <= value <= 10:
        numForInterval[1] += 1
    elif 11 <= value <= 15:
        numForInterval[2] += 1
    elif 16 <= value <= 20:
        numForInterval[3] += 1

for value in numForInterval:
    print("*"*value)