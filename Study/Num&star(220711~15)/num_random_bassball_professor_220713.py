# 교수님 버전 야구
import random

randNumList=[]
# 0 ~ 9 사이 중복 되지 않은 양의 정수 3개 생성
while len(randNumList) < 3:
    num = random.randint(0,9)
    if num not in randNumList:
        randNumList.append(num)

print("난수 값 : ",randNumList)

strikeOutCount = 0 # 삼진 횟수
gameTrialCount = 1 # 게임 시도 횟수
# 게임 시작
while True:
    inputValueList = []     # 사용자 입력 값
    strikeCount    = 0      # 스트라이크 카운트 값
    ballCount      = 0      # 볼 카운트 값

    # 사용자로 부터 양의 정수 3개 입력
    for index in range(3):
        while True:
            num = int(input("정수를 입력하세요"))
            if num not in inputValueList:
                inputValueList.append(num)
                break
    # 스트라이크, 볼 판정
    for index in range(3):
        if inputValueList[index] == randNumList[index]:
            # 스트라이크
            strikeCount += 1
        elif inputValueList[index] in randNumList:
            # 볼
            ballCount += 1

    # 삼진 또는 볼 + 스트라이크 현황 출력
    if strikeCount == 0 and ballCount == 0:
        # 삼진
        strikeOutCount += 1
        print("삼진, ", strikeOutCount," 회")
    else:
        print("Strike : ", strikeCount," Ball : ",ballCount)

    # 종료
    # 난수를 모두 맞출 경우
    if strikeCount >= 3:
        print("클리어")
        break

    # 삼진
    if strikeOutCount >= 2:
        print("삼진 2회, 종료")
        break

    # 게임 시도 횟수 5번 이상
    if gameTrialCount >= 4:
        print("게임 횟수 5이상, 종료")
        break

    gameTrialCount += 1