#  1.1 사용자로부터(키보드) 입력 받을 문자열의 라인 수 입력 후 리스트에 저장
inputValue = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))

#  1.2 검색 할 단어를 키보드로부터 입력 받고, 찾는 문자열이 있을 경우 아래와 같이 출력
inputList=[]
for value in range(inputValue):
    print(value+1,end=" ")
    inputList.append(input("번째 라인의 문자열을 입력하세요. : "))
findLine=[]
findWordCount = 0
wordCount = 0
blankCount = 0
while True:
    findWord=input("검색 할 문자열을 입력하세요. : ")
    #  1.2.1 검색 된 단어 유/무 출력, 찾는 문자열이 없을 경우 계속해서 검색 문자열 입력
    for index in range(inputValue): # N번째 문자열 라인만큼 검사하는 반복문
        if findWord in inputList[index]:
            findLine.append(index+1)
    for word in inputList: # 입력한 문자열 라인의 원소를 추출하는 반복문
        if findWord in word: # 만일 문자열 라인의 원소 안에 찾고자 하는 단어가 있으면 단어의 수, 줄, 총 검색 카운트를 증가
            for value in word:  # 원소에게서 띄워쓰기 체크
                if value == " ":
                    blankCount +=1
                    if blankCount == 1: # 1이 아닌 경우에는 연속으로 띄워쓰기가 된 것이므로 단어수는 카운트 안한다
                        # 결국 띄워쓰기가 1에서만 단어수 카운트
                        wordCount+=1
                else:
                    blankCount = 0
            find = 0 # 판별 값 변수
            for findCheck in range(len(word)): # 문자열 라인의 원소 개수만큼 체크한다
                if findWord[find] == word[findCheck]: # 만약 찾고자하는 검색 단어[판별값] == 원소의 한 단어 이라면
                    find += 1 # 판별값을 증가 시키고
                if find == len(findWord): # 이 판별값이 결국 검색 단어의 개수와 같아진다면 찾은 단어의 수를 늘리고 판별값을 초기화 시킨다
                    findWordCount += 1
                    find = 0
        if word[-1] == " ": # 마지막 원소가 띄워쓰기로 되어 있을 경우의 버그를 막기 위해 해당 값인 경우에는 감소값을 두자
                wordCount -= 1
    if findWordCount > 0: # 찾은 수가 하나라도 있으면 표출
        print(findWord,"를 찾았습니다.")
        print("검색된 라인 수 : ",findLine)
        print("검색된 횟수 : ",findWordCount)
        print("총 단어 수 : ",wordCount)
        break
    else: # 없다면 While 문 안에서 계속 반복
        print("찾을 수가 없습니다.",end=" ")