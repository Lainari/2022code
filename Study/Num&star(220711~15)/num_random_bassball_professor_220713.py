# 교수님 버전 야구
import random

randNumList=[]
# 0 ~ 9 사이 중복 되지 않은 양의 정수 3개 생성
while len(randNumList) < 3:
    num = random.randint(0,9)
    if num not in randNumList:
        randNumList.append(num)

# 게임 시작
while True:
    inputValueList = []     # 사용자 입력 값
    strikeCount    = 0      # 스트라이크 카운트 값
    ballCount      = 0      # 볼 카운트 값

    # 사용자로 부터 양의 정수 3개 입력
    for index in range(3):
        inputValueList.append(int(input(str(index+1) + "번째 정수를 입력하세요")))
    # 스트라이크, 볼 판정
    for index in range(3):
        if inputValueList[index] == randNumList[index]:
            # 스트라이크
            strikeCount += 1
        elif inputValueList[index] in randNumList:
            # 볼
            ballCount += 1

    # 삼진 또는 볼 + 스트라이크 현황 출력

    # 종료
    # 삼진
    # 게임 시도 횟수 5번 이상
    # 난수를 모두 맞출 경우