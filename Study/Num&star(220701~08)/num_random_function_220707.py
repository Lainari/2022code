# 1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
import random
randList=[]
for rand_count in range(20):
    randList.append(int((random.random()*20))+1)

# 2. List 내 원소와 원소 값에 대한 합계, 평균, 최대값, 최소값 출력
# 원소 출력
print("랜덤 값 : ")
for show in range(20):
    print(" ",randList[show]," ",end="")
print()
print()
list_avg = 0
list_sum = 0
list_max = 0
list_min = 0
# 최대 최소값 판별
list_max = randList[0]
for max_search in range(20):
    if list_max < randList[max_search]:
        list_max = randList[max_search]
print("최대 값 : ",list_max)
list_min = randList[0]
for min_search in range(20):
    if list_min > randList[min_search]:
        list_min = randList[min_search]
print("최소 값 : ",list_min)
# 합계 평균 구하고 출력
for num in range(20):
    list_sum = randList[num]+list_sum
list_avg = list_sum / 20
print("합계 : ",list_sum)
print("평균 : ",list_avg)
print()
# 3. List 내 중복 값과 중복 횟수 정보 출력[중복 값 중복 횟수]
print("중복 값\t\t중복 횟수")
overlapList=[]
for overlap1 in range(20):
    for overlap2 in range(20):
        if overlap1 == overlap2:
            pass
        elif randList[overlap1] == randList[overlap2] and randList[overlap1] not in overlapList:
            overlapList.append(randList[overlap1])
            continue
overlapCount=[]
count=0
for overlap_check in range(len(overlapList)):
    for overlap in range(20):
        if randList[overlap] == overlapList[overlap_check]:
            count+=1
    if count != 0:
        overlapCount.append(count)
    count=0
# Sort 기능 구현(정렬)
box = 0
for sort1 in range(len(overlapList)):
    for sort2 in range(len(overlapList)):
        if sort1 == sort2:
            pass
        else:
            if overlapList[sort1] > overlapList[sort2]:
                pass
            else:
                box = overlapList[sort2]
                overlapList[sort2] = overlapList[sort1]
                overlapList[sort1] = box

                box = overlapCount[sort2]
                overlapCount[sort2] = overlapCount[sort1]
                overlapCount[sort1] = box
# 출력부분
for overlapPlay in range(len(overlapList)):
    print(overlapList[overlapPlay],"\t\t",overlapCount[overlapPlay])

# 4. 구간 별 히스토그램 정보 출력[1~5 : *개, 6~10 : *개 ...]
count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
for histogram in range(20):
    if 1 <= randList[histogram] <= 5:
        count_1 += 1
    elif 6 <= randList[histogram] <= 10:
        count_2 += 1
    elif 11 <= randList[histogram] <= 15:
        count_3 += 1
    elif 15 <= randList[histogram] <= 20:
        count_4 += 1
print()
print("구간별 히스토그램")
print("1 ~ 5 : ","*"*count_1)
print("6 ~ 10 : ","*"*count_2)
print("11 ~ 15 : ","*"*count_3)
print("16 ~ 20 : ","*"*count_4)