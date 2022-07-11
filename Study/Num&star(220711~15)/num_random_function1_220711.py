# 랜덤 함수를 이용하여 아래 프로그램을 작성하라
import random
#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randList = []
for value in range(20):
    randList.append(int(random.random()*20)+1)
#  랜덤 값 출력, 가독성을 위해 2줄로 나눠 출력
print("랜덤 값 : ")
for repeat in range(20):
    print(randList[repeat],end="\t")
    if repeat == 9:
        print()
print()
#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
#  출력 순서는 최소, 최대, 합계, 평균 순
#  2-1. 변수 생성
min = randList[0]
max = randList[0]
sum = 0
avg = 0
#  최소값 구하고 출력
for check in range(20):
    if min > randList[check]:
        min = randList[check]
print("최소 값 : ",min)
#  최대값 구하고 출력
for check in range(20):
    if max < randList[check]:
        max = randList[check]
print("최대 값 : ",max)
#  합 구하고 출력
for value in range(20):
    sum = sum + randList[value]
print("합계    :",sum)
#  평균 구하고 출력
avg = sum / 20
print("평균    : ",avg)
#  3. List 내 중복 값과 중복 횟수 정보 출력
print("      중복 값  중복 회수")
#  3-1. 변수 생성
overlapList=[]
overlapCountList=[]
overlapCount=0
#  3-2. 해당 랜덤 리스트의 원소와 변수 확인 값과 같다면 카운트의 값을 증가 시키는 반복문
for overlap in range(1, 20):
    for value in range(20):
        if overlap == randList[value]:
            overlapCount += 1
        #  3-3. 반복이 끝나고 overlapCount가 2번 이상 체크됐다면 중복값이 있다는 증거므로 각 리스트에
        #  중복값과 중복회수를 저장해준다
    if overlapCount > 1:
        overlapList.append(overlap)
        overlapCountList.append(overlapCount)
    #  저장 한 후 카운트는 초기화
    overlapCount = 0
#  3-4. 반복 출력
for repeat in range(len(overlapList)):
    print("\t",overlapList[repeat],"\t",overlapCountList[repeat])
#  4. 구간 별 히스토그램 정보 출력
#  각 리스트 별 값을 파악하고 해당 범위에 있다면 각 카운트 값을 증가
count1 =0
count2 =0
count3 =0
count4 =0
for check in range(20):
    if 1 <= randList[check] <= 5:
        count1 +=1
    elif 6 <= randList[check] <= 10:
        count2 +=1
    elif 11 <= randList[check] <= 15:
        count3 +=1
    elif 15 <= randList[check] <= 20:
        count4 +=1
#  히스토그램 출력
print("1 ~ 5   : ","*"*count1)
print("6 ~ 10  : ","*"*count2)
print("11 ~ 15 : ","*"*count3)
print("16 ~ 20 : ","*"*count4)