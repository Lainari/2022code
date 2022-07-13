# - 랜덤함수를 이용하여 아래 프로그램을 작성하라
import random

#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randomList=[]
for value in range(20):
    randomList.append(random.randint(1,20))

print("랜덤 값 : ")
for repeat in range(20):
    print(randomList[repeat],end="\t")
    if repeat == 9:
        print()
print()

#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
max = 0
min = 21
sum = 0
for value in randomList:
    # 최소
    if value < min:
        min = value
    # 최대
    if value > max:
        max = value
    # 합
    sum += value
# 평균
avg = sum / len(randomList)
print("최소 값 : ",min)
print("최대 값 : ",max)
print("합계    : ",sum)
print("평균    : ",avg)

#  3. List 내 중복 값과 중복 횟수 정보 출력
print("중복 값   중복 회수")
overlapList=[]
overlapCount=[0]*20

# 리스트 원소가 중복 리스트에 있는지 확인
for check in randomList:
    if check in overlapList: # 있으면 해당 중복 값의 회수를 1씩 증가
        overlapCount[check-1] += 1
        # 단, 중복 값이 1~20 이므로 중복 회수 리스트의 원소(0~19)번째를 1씩 증가 시켜준다
    else:
        # 없으면 중복 리스트에 append
        overlapList.append(check)
# 중복 값과 회수 출력
index = 1
for value in overlapCount:
    # 만일 중복 회수가 1 이상이라면(적어도 카운트가 2번 된 경우)
    if value>=1:
        print(" ",index,"\t    ",value+1) # 그 값과 카운트 값을 출력(단, 카운트 값을 1씩 증가 시켜야지만 해당 중복 횟수가 나옴)
    index += 1
#  4. 구간 별 히스토그램 정보 출력
starList=[0]*4
for value in randomList:
    if 1<=value<=5:
        starList[0] += 1
    elif 6<=value<=10:
        starList[1] += 1
    elif 11<=value<=15:
        starList[2] += 1
    elif 15<=value<=20:
        starList[3] += 1
count = 1
for repeat in range(len(starList)):
    print(((count-1)*5)+1," ~ ",(count*5)," : ","*"*starList[repeat])
    count+=1