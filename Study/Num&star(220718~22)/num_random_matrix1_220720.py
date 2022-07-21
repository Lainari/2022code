# 1. 1~50 사이의 중복되지 않은 정수형 난수 25개를 선택하여 LIST에 저장
import random

randList=[]

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
        check.append(randList[(col*5)+row])
        if len(check) == 5:
            for a in range(len(check)):
                for b in range(len(check)):
                    if a != b:
                        if check[a] > check[b]:
                            temp = check[a]
                            check[a] = check[b]
                            check[b] = temp  
                            temp = 0
            rowList.append(check)
            check=[]
print("열 기준 최대값 : ",end=" ")
for row in range(5):
    print(rowList[row][0],end="  ")
print("열 기준 최소값 : ",end=" ")
for row in range(5):
    print(rowList[row][4],end="  ")
print("열 기준 중간값 : ",end=" ")
for row in range(5):
    print(rowList[row][len(rowList[row])//2],end="  ")
print()
print("="*100)
# 2) 행 기준
colList=[]
colMaxList=[]
colMinList=[]
for row in range(5):
    check=[]
    for col in range(5):
        check.append(randList[(row*5)+col])
        if len(check) == 5:
            for a in range(len(check)):
                for b in range(len(check)):
                    if a != b:
                        if check[a] > check[b]:
                            temp = check[a]
                            check[a] = check[b]
                            check[b] = temp  
                            temp = 0
            colList.append(check)
            check=[]
print("행 기준 최대값 : ",end=" ")
for row in range(5):
    print(colList[row][0],end="  ")
print("행 기준 최소값 : ",end=" ")
for row in range(5):
    print(colList[row][4],end="  ")
print("행 기준 중간값 : ",end=" ")
for row in range(5):
    print(colList[row][len(colList[row])//2],end="  ")
print()
print("="*100)
# 3. LIST 전체를 기준으로 최대, 최소, 중간 값을 출력하라.
allList=[]
for col in range(25):
    allList.append(randList[col])
    if len(allList) == 25:
        for a in range(len(allList)):
            for b in range(len(allList)):
                if a != b:
                    if allList[a] > allList[b]:
                        temp = allList[a]
                        allList[a] = allList[b]
                        allList[b] = temp  
                        temp = 0
print("전체 기준 최대값 : ",end=" ")
print(allList[0],end="  ")
print("전체 기준 최소값 : ",end=" ")
print(allList[-1],end="  ")
print("전체 기준 중간값 : ",end=" ")
print(allList[len(allList)//2],end="  ")