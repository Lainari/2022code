# - 랜덤함수를 이용하여 아래 프로그램을 작성하라
import random
#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randList=[]
for value in range(20):
    randList.append(int(random.random()*20)+1)
#  1-1 랜덤 값 출력 (가독성을 위해 띄워쓰기 포함)
print("랜덤 값 : ")
for value in range(20):
    print(randList[value],"\t",end="")
    if value == 9:
        print()
print()
print("="*100)
#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
# 변수 생성
min = randList[0]
max = randList[0]
sum = 0
avg = 0
#  2-1. 최소, 최대, 합, 평균 순으로 출력
#  최소값
for min_check in range(20):
    if min > randList[min_check]:
        min = randList[min_check]
print("최소 값 : ",min)
#  최대 값
for max_check in range(20):
    if max < randList[max_check]:
        max = randList[max_check]
print("최대 값 : ",max)
#  합계
for repeat in range(20):
    sum = sum + randList[repeat]
print("합계    : ",sum)
#  평균
avg = sum / 20
print("평균    : ",avg)
print("="*100)
#  3. List 내 중복 값과 중복 횟수 정보 출력 [ 아래 출력 결과 참조 ]
#  변수 생성
overlapList=[]
overlapCountList=[]
overlapCount = 0
#  반복 체크 변수를 통해 해당 값과 랜덤 값이 같을 경우 반복 COUNT 증가, 그 중에서 2 이상인 값들은
#  전부 2회 이상 반복 했으므로 반복리스트에 추가 및 카운트 리스트에도 추가해준다
for overlapCheck in range(1,20):
    for value in range(20):
        if overlapCheck == randList[value]:
            overlapCount += 1
    if overlapCount > 1:
        overlapList.append(overlapCheck)
        overlapCountList.append(overlapCount)
    overlapCount = 0
print("중복 값     중복 회수")
for value in range(len(overlapList)):
    print("  ",overlapList[value],"\t\t",overlapCountList[value])
print("="*100)
#  4. 구간 별 히스토그램 정보 출력 [ 아래 출력 결과 참조 ]
#  변수 생성
count1=0
count2=0
count3=0
count4=0
#  랜덤 리스트를 조사하여 해당 값 범위에 맞게 count 값들을 증가시킨다
for value in range(20):
    if 1 <= randList[value] <=5:
        count1+=1
    elif 6 <= randList[value] <=10:
        count2+=1
    elif 11 <= randList[value] <=15:
        count3+=1
    elif 15 <= randList[value] <=20:
        count4+=1
#  해당 값에 맞게 별들을 출력한다
print("1 ~ 5   : ","*"*count1)
print("6 ~ 10  : ","*"*count2)
print("11 ~ 15 : ","*"*count3)
print("16 ~ 20 : ","*"*count4)