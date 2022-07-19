# 줄 수 입력
lineNum = int(input("줄 수 입력해주세요 : "))

inputLine=[]

# 줄 수만큼 문자열 저장
for index in range(lineNum):
    inputLine.append(input(str(index+1)+"번째 문자열을 입력하세요 : "))


# 찾고자 하는 문자열이 나올 때까지 반복
while True:
    findLine=[]
    findList=input("찾고싶은 문자열을 입력하세요 : ")
    wordCount = 0
    findCount = 0

    for line in range(lineNum):
        indexValue = 0
        nextWord=""
        preWord=""
        findCheck = 0

        for word in range(len(inputLine[line])):

            if word == (len(inputLine[line])-1):
                nextWord=""
            else:
                nextWord=inputLine[line][word+1]

            # 매칭 시작
            if inputLine[line][word] == findList[indexValue] and indexValue == 0:
                indexValue += 1

            # 매칭 중
            elif inputLine[line][word] == findList[indexValue]:
                # 매칭 완료
                if indexValue == (len(findList) -1) and ((preWord == findList[indexValue-2]) and (nextWord==" " or nextWord=="")):
                    findCount += 1
                    indexValue = 0
                    findCheck += 1

                elif indexValue == (len(findList)-1):
                    indexValue = 0

                # 매칭 지속
                else:
                    indexValue += 1

            # 매칭 실패
            else:
                indexValue = 0
            preWord = inputLine[line][word]

            # 단어 판별
            if nextWord == " " or nextWord=="":
                wordCount += 1

        if findCheck >= 1:
            findLine.append(line+1)

    if findCount >= 1:
        print(findList,"를 찾았습니다")
        print("검색된 라인 : ",findLine)
        print("검색된 횟수 : ",findCount)
        print("총 단어 수 : ",wordCount)
        break
    else:
        print("찾지 못했습니다.",end=" ")