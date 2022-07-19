# 두 가지 방법
# 1) sort API 사용
# 2) 구글링 -> 버블 소팅, 퀵 소팅
#=======================================================================================#
# 1. 1~50 사이의 중복되지 않은 정수형 난수 25개를 선택하여 LIST에 저장
import random
randList=[]
rowTableList=[]
colTableList=[]

# 랜덤 수 생성
while True:
    check = random.randint(1,50)
    if check not in randList:
        randList.append(check)
            
    if len(randList) >= 25:
        break
# 테이블에 합치기
for value in range(len(randList)):
    colTableList.append(randList[value])
    if (value+1) % 5 == 0:
        rowTableList.append(colTableList)
        colTableList=[]
print("랜덤 테이블")
print("-"*100)
# 테이블 표출
for row in range(5):
    for col in range(5):
        print(rowTableList[row][col],end="\t")
    print()
print("-"*100)

# 2. 각 열, 행 별 최대, 최소, 중간 값을 찾아 출력하라.
#=======================================================================================#
# 1) 열 기준
rowList=[]
rowData=[]
for value in range(5):
    for index in range(5):
        rowData.append(rowTableList[index][value])
        if len(rowData)>=5:
            rowList.append(rowData)
            rowData=[]

colMaxList=[]
colMinList=[]

for row in range(5):
    colMax = 0
    colMin = 51
    for col in range(5):
        if colMax < rowList[row][col]:
            colMax = rowList[row][col]
        if colMin > rowList[row][col]:
            colMin = rowList[row][col]
    colMaxList.append(colMax)
    colMinList.append(colMin)

for table in range(5):
    for row in range(5):
        for col in range(5):
            temp=0
            if col > 0:
                if rowList[row][col] > rowList[row][col-1]:
                    temp = rowList[row][col]
                    rowList[row][col] = rowList[row][col-1]
                    rowList[row][col-1] = temp
                    temp = 0
# #=======================================================================================#
# # 2) 행 기준
colList=[]
colData=[]
for value in range(5):
    for index in range(5):
        colData.append(rowTableList[value][index])
        if len(colData)>=5:
            colList.append(colData)
            colData=[]

rowMaxList=[]
rowMinList=[]

for row in range(5):
    rowMax = 0
    rowMin = 51
    for col in range(5):
        if rowMax < colList[row][col]:
            rowMax = colList[row][col]
        if rowMin > colList[row][col]:
            rowMin = colList[row][col]
    rowMaxList.append(rowMax)
    rowMinList.append(rowMin)

for table in range(5):
    for row in range(5):
        for col in range(5):
            temp=0
            if col > 0:
                if colList[row][col] > colList[row][col-1]:
                    temp = colList[row][col]
                    colList[row][col] = colList[row][col-1]
                    colList[row][col-1] = temp
                    temp = 0

print("열의 최소값 : ")
for repeat in range(5):
    print(colMinList[repeat],end="\t")
print()
print("열의 최대값 : ")
for repeat in range(5):
    print(colMaxList[repeat],end="\t")
print()
print("열의 중간값 : ")
mid = 2
for repeat in range(5):
    print(rowList[repeat][mid],end="\t")
print()
print("-"*100)

print("행의 최소값 : ")
for repeat in range(5):
    print(rowMinList[repeat],end="\t")
print()
print("행의 최대값 : ")
for repeat in range(5):
    print(rowMaxList[repeat],end="\t")
print()
print("행의 중간값 : ")
mid = 2
for repeat in range(5):
    print(colList[repeat][mid],end="\t")
print()
print("-"*100)
# #=======================================================================================#
# # 3. LIST 전체를 기준으로 최대, 최소, 중간 값을 출력하라.