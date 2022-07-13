# - 랜덤함수를 이용하여 아래 프로그램을 작성하라
import random

#  1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
randomList=[]
for value in range(20):
    randomList.append(random.randint(1,20))

# 랜덤 값 표출
print("랜덤 값 : ")
for repeat in range(20):
    print(randomList[repeat],end="\t")
    if repeat == 9:
        print()
print()

#  2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
sum = 0
max = 0
min = 21

# 랜덤리스트 원소 값 추출
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

# 최소, 최대, 합, 평균 출력
print("최소 값 : ",min)
print("최대 값 : ",max)
print("합계    : ",sum)
print("평균    : ",avg)

#  3. List 내 중복 값과 중복 횟수 정보 출력

# 중복 값과 중복 횟수 저장 리스트 생성
overlapList = []
overlapCount = [0]*len(randomList)

# 중복 값 판별
for value in randomList:
    # 만약 랜덤 추출값이 중복 값에 포함되었는가?
    if value in overlapList:
        # 그렇다면 중복 횟수에 카운트를 해주는데, value - 1번째에 1씩 카운트 해준다
        overlapCount[value-1] += 1
    else: # 그렇지 않다면 overlapList에 append 해주기
        overlapList.append(value)

# 중복값과 횟수 출력
print("중복 값   중복 횟수")
index = 1
for repeat in overlapCount:
    # 만약 overlapCount 값이 1 이상이라면(최소 중복 2회) 출력
    if repeat >= 1:
        print("  ",index,"\t     ",repeat+1)
        # 단, overlapCount 는 1회이지만 중복은 2회 했으므로 repeat 값을 1씩 증가시켜 표출한다
    # 끝나면 index 값 증가
    index += 1

#  4. 구간 별 히스토그램 정보 출력
starList = [0]*4
for check in randomList:
    if 1 <= check <= 5:
        starList[0] += 1
    elif 6 <= check <= 10:
        starList[1] += 1
    elif 11 <= check <= 15:
        starList[2] += 1
    elif 16 <= check <= 20:
        starList[3] += 1
count = 1
for value in starList:
    print(((count-1)*5)+1,"~",count*5," : ","*"*value)
    count+=1