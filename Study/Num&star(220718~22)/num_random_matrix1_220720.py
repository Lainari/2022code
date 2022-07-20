# 1. 1~50 사이의 중복되지 않은 정수형 난수 25개를 선택하여 LIST에 저장
import random

randList=[45, 10, 30, 36, 38, 43, 3, 46, 40, 2, 16, 19, 17, 37, 26, 21, 27, 29, 28, 31, 34, 12, 49, 44, 41]

while len(randList) < 25:
    check = random.randint(1,50)
    if check not in randList:
        randList.append(check)
print("랜덤 리스트 입니다")
print("="*100)
for row in range(5):
    for col in range(5):
        print(randList[col+(5*row)],end="\t")
    print()
print("="*100)
# 2. 각 열, 행 별 최대, 최소, 중간 값을 찾아 출력하라.
# 1) 열 기준
rowList=[]
rowMaxList=[]
rowMinList=[]
for row in range(5):
    check=[]
    for col in range(5):
        if col > 0:
            check.append(randList[(col*5)+row])
        if len(check) == 5:
            rowList.append(check)

# 2) 행 기준

# 3. LIST 전체를 기준으로 최대, 최소, 중간 값을 출력하라.