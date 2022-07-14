# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random

gameList=[]
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

playCount = 0
strikeOut = 0
while True:
    playCount += 1
# • 아래 경우 게임 Lose – 시도 횟수 >= 5 – Strike out == 2
    if playCount >= 5:
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList,"입니다")
        break
    elif strikeOut == 2:
        print("2스트라이크 아웃~!!")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList,"입니다")
# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
    print("시도횟수 : ",playCount)
    print("정수 3개를 입력하세용~~^_^")
    playerList=[]
    while len(playerList) < 3:
        playerList.append(int(input()))
# 스트라이크, 볼, 아웃 판별식
    strike = 0
    ball = 0
    for check in range(3):
        if playerList[check] in gameList:
            if playerList[check] == gameList[check]:
                strike+=1
            else:
                ball += 1
# • 아래 경우 게임 Win – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우
    if strike == 3:
        print("삼진~~!!! 축하드립니다!")
        print("정답은 : ",gameList,"입니다")
        print("입력값 : ",playerList)
    elif strike == 0 and ball == 0:
        strikeOut += 1
        if strikeOut == 1:
            print("Out : 아웃 1번")
    else:
        if strike > 0:
            print(strike," Strike",end=" ")
        if ball > 0:
            print(ball," Ball",end=" ")
    print()