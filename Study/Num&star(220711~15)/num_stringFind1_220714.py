#  1.1 사용자로부터(키보드) 입력 받을 문자열의 라인 수 입력 후 리스트에 저장
inputValue = int(input("입력 문자열의 줄(Line) 수를 입력하세요! : "))

#  1.2 검색 할 단어를 키보드로부터 입력 받고, 찾는 문자열이 있을 경우 아래와 같이 출력
inputList=[]
for value in range(inputValue):
    print(value+1,end=" ")
    inputList.append(input("번째 라인의 문자열을 입력하세요. : "))
findWord=[]
#  1.2.1 검색 된 단어 유/무 출력, 찾는 문자열이 없을 경우 계속해서 검색 문자열 입력
#  1.2.2 검색 된 단어의 줄, 총 검색 횟수 출력
#  1.3 입력받은 문자열의 단어 개수 카운트 후 출력 