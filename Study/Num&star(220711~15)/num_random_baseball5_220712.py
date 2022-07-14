#게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random

gameList=[]
check = 0

while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)
# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
playCount = 1
strikeOut = 0
while True:
    print("시도횟수 : ",playCount)
    playerList=[]
    print("정수 3개를 입력하세용~~^_^")
    while len(playerList) < 3:
        playerList.append(int(input()))
    strike = 0
    ball = 0
    for value in range(3):
        if playerList[value] not in gameList:
            continue
        else:
            if playerList[value] == gameList[value]:
                strike += 1
            else:
                ball += 1
    if strike == 0 and ball == 0:
        strikeOut += 1
        if strikeOut > 1:
            print("2 스트라이크 아웃! ㅠㅠ")
            print("아까비~~~졌네용..")
            print("정답은 : ",gameList,"입니다.")
            break
        else:
            print("Out : 아웃 1번")
    elif strike == 3:
        print("승리~~!!")
        print("정답은 : ",gameList,"입니다.")
        break
    else:
        if strike > 0:
            print(strike," Strike",end=" ")
        if ball > 0:
            print(ball," Ball",end=" ")
        playCount += 1
        if playCount > 4:
            print("게임횟수 초과")
            print("아까비~~~졌네용..")
            print("정답은 : ",gameList,"입니다.")
            break
# • 아래 경우 게임 Lose – 시도 횟수 >= 5 – Strike out == 2
# • 아래 경우 게임 Win – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우