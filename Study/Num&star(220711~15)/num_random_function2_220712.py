# - 랜덤함수를 이용하여 아래 프로그램을 작성하라 
import random
#   1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randomList = []
for value in range(20):
    randomList.append(random.randint(1,20))

#   2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
sum = 0
max = 0
min = 21

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

print(sum,avg, max, min)

#   3. List 내 중복 값과 중복 횟수 정보 출력
overlapList=[]
overlapCount=[0]*len(randomList)

for value in randomList:
    if value in overlapList: # 만일 randomList의 원소가 중복리스트에 포함 되어있다면
        overlapCount[value-1] += 1 # 중복 횟수 리스트의 원소의 값 번째에서 1 값을 증가시킨다
    else:
        overlapList.append(value) # 없다면 추가해준다

index = 1 # 검사를 도울 index 값
for value in overlapCount: # 중복 리스트의 값을 불러온다
    if value >= 1: # 여기서 중복 리스트의 값이 1 이상인 경우
        print(index, value+1) # 해당 원소의 값(검사를 도울 index 값)을 출력하고
        # 순번이 하나씩 밀렸기때문에 value 값을 1씩 증가시켜준다
    
    index += 1 # 위 해당 사항이 없다면 index 값을 증가시켜준다

#   4. 구간 별 히스토그램 정보 출력
starList=[0]*4
for value in randomList:
    if 1 <= value <= 5:
        starList[0] += 1
    elif 6<= value <= 10:
        starList[1] += 1
    elif 11<= value <= 15:
        starList[2] += 1
    elif 15<= value <= 20:
        starList[3] += 1

for value in starList:
    print("*"*value)