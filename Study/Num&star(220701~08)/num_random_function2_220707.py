# 1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
import random
ranList = []

for value in range(20):
    ranList.append(random.randint(1,20))
# 2. List 내 원소와 원소 값에 대한 합계, 평균, 최대값, 최소값 출력
sum = 0
avg = 0
max = ranList[0]
min = ranList[0]
# 최대 최소값 판별
for value in range(20):
    if ranList[value] > max:
        max = ranList[value]

for value in range(20):
    if ranList[value] < min:
        min = ranList[value]
# 합계 평균 구하고 출력
for value in range(20):
    sum = sum + ranList[value]
avg = sum / 20

print("랜덤 값 : ")
for listPrint in range(20):
    print(ranList[listPrint],"\t",end="")
print()
print("="*150)
print("최소 값 : ",min)
print("최대 값 : ",max)
print("합계    : ",sum)
print("평균    : ",avg)
print("="*150)
# 3. List 내 중복 값과 중복 횟수 정보 출력[중복 값 중복 횟수]
overlapList = []
overlapCount = []
count = 0
print("중복 값 \t중복 회수")

# 중복값 찾기
for Overlap in range(20):
    for overlap in range(20):
        if Overlap == overlap:
            continue
        elif ranList[Overlap] == ranList[overlap] and ranList[Overlap] not in overlapList:
            overlapList.append(ranList[Overlap])
            continue
# 중복 회수 구하기
for Overlap in range(len(overlapList)):
    for overlap in range(20):
        if overlapList[Overlap] == ranList[overlap]:
            count +=1
    overlapCount.append(count)
    count = 0
# 중복값과 중복 회수를 순서대로 정렬할 것, sort 사용 X
box = 0
for Check in range(len(overlapList)):
    for check in range(len(overlapList)):
        if Check == check:
            continue
        elif overlapList[Check] < overlapList[check]:
            box = overlapList[check]
            overlapList[check] = overlapList[Check]
            overlapList[Check] = box
            box = 0
            box = overlapCount[check]
            overlapCount[check] = overlapCount[Check]
            overlapCount[Check] = box
# 중복값과 회수 출력
for value in range(len(overlapList)):
    print(overlapList[value],"\t\t",overlapCount[value])
print("="*150)
# 4. 구간 별 히스토그램 정보 출력[1~5 : *개, 6~10 : *개 ...]
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for check in range(20):
    if 1 <= ranList[check] <=5:
        count1 +=1
    elif 6 <= ranList[check] <=10:
        count2 +=1
    elif 11 <= ranList[check] <= 15:
        count3 +=1
    elif 16 <= ranList[check] <= 20:
        count4 +=1
print("구간별 히스토그램")
print("1 ~ 5 : ","*"*count1)
print("6 ~ 10 : ","*"*count2)
print("11 ~ 15 : ","*"*count3)
print("16 ~ 20 : ","*"*count4)
print("="*150)