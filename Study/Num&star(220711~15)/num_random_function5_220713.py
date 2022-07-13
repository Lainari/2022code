# - 랜덤함수를 이용하여 아래 프로그램을 작성하라
import random
#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randList=[]
for value in range(20):
    randList.append(random.randint(1,20))
print("랜덤 값 : ")
for repeat in range(20):
    print(randList[repeat],end="\t")
    if repeat == 9:
        print()
print()
#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
sum = 0
min = 21
max = 0
for value in randList:
    if value < min:
        min = value
    if value > max:
        max = value
    sum += value
avg = sum / len(randList)
print("최소값 : ",min)
print("최대값 : ",max)
print("합계   : ",sum)
print("평균   : ",avg)
#  3. List 내 중복 값과 중복 횟수 정보 출력
overlapList=[]
overlapCount=[0]*20

for value in randList:
    if value in overlapList:
        overlapCount[value-1] += 1
    else:
        overlapList.append(value)

print("중복값   중복횟수")
index = 1
for value in overlapCount:
    if value >= 1:
        print(" ",index,"\t   ",value+1)
    index+=1
#  4. 구간 별 히스토그램 정보 출력
starList = [0]*4
for value in randList:
    if 1<=value<=5:
        starList[0] += 1
    elif 6<= value <=10:
        starList[1] += 1
    elif 11<= value <=15:
        starList[2] += 1
    elif 16<= value <=20:
        starList[3] += 1
count = 1
for repeat in starList:
    print(((count-1)*5)+1," ~ ",(count*5)," : ","*"*repeat)
    count+=1