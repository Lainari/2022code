# 줄 수를 입력
inputNum = int(input("문자열 수를 입력해주세요 : "))

inputList=[]
# 해당 줄 수 만큼 문자열 입력
for index in range(inputNum):
    inputList.append(input(str(index+1)+" 번째 문자열 입력 : "))

# 검색 수가 1개 이상 될 때 까지 반복
while True:
    findCount = 0
    findLine = []
    wordCount = 0

    # 검색할 문자열 입력
    findWord=input("찾고 싶은 문자열을 입력해주세요 : ")

    # 검색 시작
    for row in range(inputNum):

        indexValue = 0
        findLineCount = 0
        nextWord=""
        preWord=""

        for col in range(len(inputList[row])):
            # 다음 단어 검색 후 입력
            if col == (len(inputList[row])-1):
                nextWord=""
                wordCount += 1
            else:
                nextWord=inputList[row][col+1]
                if (inputList[row][col] != " " and nextWord == " " and col+1 != len(inputList[row])-1):
                    wordCount += 1

            # 검색 진행
            if findWord[indexValue] == inputList[row][col] and indexValue == 0:
                indexValue += 1

            elif findWord[indexValue] == inputList[row][col]:

                # 검색 끝
                if indexValue == (len(findWord)-1) and (preWord==findWord[indexValue-2] and (nextWord=="" or nextWord==" ")):
                    findCount += 1
                    indexValue = 0
                    findLineCount += 1

                # 검색 지속
                else:
                    if indexValue <= 3:
                        indexValue += 1
                    else:
                        indexValue = 0

            # 검색 불가
            else:
                indexValue = 0
    
            # 이전 단어는 현재 단어로 보충
            preWord = inputList[row][col]

        # 검색된 라인 입력
        if findLineCount >= 1:
            findLine.append(row+1)

    # 탈출 조건
    if findCount >= 1:
        print("찾은 단어 수 : ",findCount)
        print("발견 줄(번호) : ",findLine)
        print("총 단어 수 : ",wordCount)
        break
    else:
        print("재입력이 요구됩니다.",end=" ")