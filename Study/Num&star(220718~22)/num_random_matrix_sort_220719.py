# 1. 1~50 사이의 중복되지 않은 정수형 난수 25개를 선택하여 LIST에 저장
import random

myList=[]

while len(myList) <= 24:
    check = random.randint(1,50)
    if check not in myList:
        myList.append(check)

# 2. 각 열, 행 별 최대, 최소, 중간 값을 찾아 출력하라.
print("랜덤 리스트")
print("="*100)
for row in range(25):
    print(myList[row],end="\t")
    if (row+1)%5 == 0:
        print()
print("="*100)
# 1) 열 기준
colMaxList=[]
colMinList=[]
colMidList=[]
colList=[]
for row in range(5):
    checkList =[]
    for col in range(5):
        if (row*(5+col)) % (5+col) == 0:
            checkList.append(myList[(5*col)+row])
    checkList.sort()
    colMinList.append(checkList[0])
    colMaxList.append(checkList[-1])
    colMidList.append(checkList[len(checkList)//2])
    colList.append(checkList)
# 2) 행 기준
rowMaxList=[]
rowMinList=[]
rowMidList=[]
rowList=[]
for row in range(5):
    checkList =[]
    for col in range(5):
        if (col*(5+row)) % (5+row) == 0:
            checkList.append(myList[(5*row)+col])
    checkList.sort()
    rowMinList.append(checkList[0])
    rowMaxList.append(checkList[-1])
    rowMidList.append(checkList[len(checkList)//2])
    rowList.append(checkList)
for index in range(15):
    if index == 0:
        print("열의 최소값 : ",end=" ")
    if 0 <= index <= 4:
        print(colMinList[index],end="   ")
    if index == 5:
        print()
        print("열의 최대값 : ",end=" ")
    if 5<= index <= 9:
        print(colMaxList[index-5],end="   ")
    if index == 10:
        print()
        print("열의 중간값 : ",end=" ")
    if 10<= index <= 14:
        print(colMidList[index-10],end="   ")
print()
print("="*100)
for index in range(15):
    if index == 0:
        print("행의 최소값 : ",end=" ")
    if 0 <= index <= 4:
        print(rowMinList[index],end="   ")
    if index == 5:
        print()
        print("행의 최대값 : ",end=" ")
    if 5<= index <= 9:
        print(rowMaxList[index-5],end="   ")
    if index == 10:
        print()
        print("행의 중간값 : ",end=" ")
    if 10<= index <= 14:
        print(rowMidList[index-10],end="   ")
print()
print("="*100)
# 3. LIST 전체를 기준으로 최대, 최소, 중간 값을 출력하라.
myList.sort()
print("테이블의 최소값 : ",end=" ")
print(myList[0])
print("테이블의 최대값 : ",end=" ")
print(myList[-1])
print("테이블의 중간값 : ",end=" ")
print(myList[len(myList)//2])
print()