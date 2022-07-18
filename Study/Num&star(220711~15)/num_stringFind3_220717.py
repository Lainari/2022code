# 입력 할 문자열 개수 파악
inputValue = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))

# 줄 수만큼 영문 문자열을 list에 저장
inputList=[]
count = 0

for value in range(inputValue):
    count += 1
    print(count,end=" ")
    inputList.append(input("번째 문자열을 입력해주세요. : "))

findLine = []
wordList = []

# 찾고 싶은 문자열은 검색될 때 까지 지속된다
while True:
    findList=input("검색 할 문자열을 입력해주세요 : ")
    count = 1
    findWordCount = 0

    # 문자열 검색
    for line in inputList:
        lineCount = 0

        # 단어 검색(단어 수와 찾고 싶은 문자열 개수 파악) & 찾고 싶은 단어가 단어 리스트에 있는지 확인  
        sum = ""                        # 문자열을 붙이기 위한 변수 생성
        for word in line:               # 문자열 안에 단어들을 검사
            if word != " ":             # 만약 문자열 이 공백이 아니라면 단어를 이어붙이고
                sum += word

            else:
                if sum !="":            # 공백이긴 하나 연속된 공백이라면 이어붙이지 않는다
                    wordList.append(sum)
                    if findList == sum: # 만일 단어가 내가 찾는 단어라면
                        lineCount += 1  # 검색된 라인을 검사하는 변수 값을 증가
                        findWordCount += 1 # 찾은 문자의 개수를 증가 시킨다 
                sum=""                  # 다 끝나면 이어붙임 변수는 초기화                
                
        if sum != " " and sum != "":    # 반복이 종료 될 때 마지막으로 남아있는 단어를 붙여준다(단, 공백은 안붙임)
            wordList.append(sum)
            if findList == sum:         # 이 구간에서도 검색된 라인을 검사하는 변수 값을 증가시킴으로 추후 발생 문제를 막는다
                lineCount += 1
                findWordCount += 1      # 찾은 문자의 개수를 증가 시킨다 
                
        # 문자열 안에 검색할 문자열이 있는가? 있다면 줄 넘버리스트에 저장
        if lineCount >= 1:
            findLine.append(count)
        count+=1
        
    # ---------------------------------------검출 끝---------------------------------------#

    # 찾고싶은 단어와 해당 단어 검색 수, 총 단어의 수를 구했으니 탈출하자, 조건은 찾고 싶은 단어 검출 수가 1이상
    if findWordCount >=1:
        print(findList,"를 찾았습니다.")
        print("검색된 라인 : ",findLine)
        print("검색된 횟수 : ",findWordCount)
        print("총 단어 수 : ",len(wordList))
        break
    else:
        print("찾을 수가 없습니다.",end=" ")