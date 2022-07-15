inputNum = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))
# 영문 문자열을 키보드로부터 입력 받아 List에 저장
inputList=[]
findCountList=[]
for index in range(inputNum):
    print(index+1,end=" ")
    inputList.append(input("번째 라인의 문자열을 입력하세요. : "))
# 해당 단어가 있을 경우 결과 값 출력
while True:
    # 검색 단어를 키보드로부터 다시 입력 받기
    findList=input("검색 할 문자열을 입력하세요. : ")
    findCount = 0
#  - 검색된 단어 유/무
    for word in inputList:
        if findList in word:
            findCount += 1
            findCountList.append(findCount)
    if findCount >= 1:
        #  - 검색된 단어의 줄, 총 검색 횟수 출력
        break
    else:
        print("찾을 수가 없습니다.",end=" ")



# 입력 받은 문자열의 단어 개수 카운트 후 출력
print(findList," 를 찾았습니다.")
print("검색된 라인 수 : ",findCountList)
print("검색된 횟수 : ")
print("총 단어 수 : ")