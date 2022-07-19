# 줄 수 입력
lineNum=int(input("줄 수를 입력하세요 : "))

textList=[]
findCount = 0
findLine=[]
wordCount = 0
# 영문 입력
for index in range(lineNum):
    textList.append(input(str(index+1)+"번째 문자열을 입력해주세요. : "))

# 찾고 싶은 문자열 입력, 찾고 싶은 문자열이 없을 경우 계속 반복
while True:
    findList=input("찾고 싶은 문자열을 입력해주세요 : ")
    for line in range(lineNum):                     # 줄 생성
        findCheck = 0
        preWord=""                                  # 앞 단어 변수
        nextWord=""                                 # 뒤 단어 변수
        indexNum = 0                                # 매칭 변수
        for word in range(len(textList[line])):     # 단어 생성
            if word == (len(textList[line])-1):    # 뒤 단어 변수 값 지정
                nextWord = ""
            else:
                nextWord = textList[line][word+1]

            # 매칭 시작
            if textList[line][word] == findList[indexNum] and indexNum==0:
                indexNum += 1
            # 매칭 중
            elif textList[line][word] == findList[indexNum]:

                # 매칭 완료
                if indexNum == (len(findList) -1) and (preWord==findList[indexNum-2] and (nextWord==" " or nextWord=="")):
                    findCount += 1
                    findCheck += 1
                    indexNum = 0

                elif indexNum == (len(findList)-1):
                    indexNum = 0

                # 매칭 계속
                else:
                    indexNum += 1

            # 매칭 실패
            else:
                indexNum = 0
            preWord=textList[line][word]
            
            # 단어 판별
            if nextWord == " " or nextWord=="":
                wordCount += 1

        if findCheck >= 1:
            findLine.append(line+1)

    if findCount >= 1:
        print(findList,"를 찾았습니다.")
        print("검색된 라인 : ",findLine)
        print("검색된 횟수 : ",findCount)
        print("총 단어 수 : ",wordCount)
        break
    else:
        print("찾을 수가 없습니다.",end=" ")