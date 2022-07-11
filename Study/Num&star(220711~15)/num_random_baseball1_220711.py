# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random

gameList = []
check = 0

while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
play = True
while play:
    playCount = 1
    playerList = []

    print("정수 3개를 입력하세용~~^_^")
    while len(playerList) < 3:
        playerList.append(int(input()))
    
# 스트라이크, 볼, 아웃 판별식 작성
    strikeOut = 0
    for check in range(3):
        strike = 0
        ball =0

        if playerList[check] == gameList[check]:
            strike += 1
            if strike == 3: # strike 3가 되면 탈출
                play = False

        elif playerList[check] in gameList:
            ball += 1
        
        if strike == 0 and ball == 0:
            strikeOut += 1
            if strikeOut == 1:
                print("Out : 아웃 1번")
            else: # strikeOut 2가 되면 탈출
                play = False
    playCount += 1
    if playCount == 5:
        play = False # playCount가 5가 되면 탈출
# • 아래 경우 게임 Lose – 시도 횟수 >= 5 or – Strike out == 2
# • 아래 경우 게임 Win – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우