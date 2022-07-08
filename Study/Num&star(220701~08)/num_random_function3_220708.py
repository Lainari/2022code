#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
import random
randList = []
for value in range(20):
    randList.append(random.randint(1,20))
#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
#       랜덤값 / 최소 값 / 최대 값 / 합계 / 평균 순으로 출력
print("랜덤 값 : ")
for value in range(20):
    print(randList[value], end="  ")
print()
print("="*150)
sum = 0
min = randList[0]
max = randList[0]
for check in range(20):
    if min > randList[check]:
        min = randList[check]
    if max < randList[check]:
        max = randList[check]
print("최소 값 : ",min)
print("최대 값 : ",max)
for plus in range(20):
    sum = sum + randList[plus]
avg = sum/20
print("합계    : ",sum)
print("평균    : ",avg)
print("="*150)
#  3. List 내 중복 값과 중복 횟수 정보 출력
overlapList=[]
overlapCount = 0
countList=[]
checkData = 1
# 중복 값 검색
for value in range(20):
    for value in range(20):
        if randList[value] == checkData:
            overlapCount += 1
    if overlapCount > 1:
        overlapList.append(checkData)
        countList.append(overlapCount)
    overlapCount = 0
    checkData +=1
print("       중복 값", "중복 회수")
for value in range(len(overlapList)):
    print("\t",overlapList[value],"\t",countList[value])
#  4. 구간 별 히스토그램 정보 출력
count1 = 0
count2 = 0
count3 = 0
count4 = 0
for value in range(20):
    if 1<= randList[value] <= 5:
        count1 +=1
    elif 6<= randList[value] <= 10:
        count2 +=1
    elif 11<= randList[value] <= 15:
        count3 +=1
    elif 16<= randList[value] <= 20:
        count4 +=1
print("구간별 히스토그램")
print("   1 ~ 5   : ","*"*count1)
print("   6 ~ 10  : ","*"*count2)
print("   11 ~ 15 : ","*"*count3)
print("   16 ~ 20 : ","*"*count4)