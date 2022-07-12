# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random
play = True
gameList = []
check = 0

# 게임 리스트 생성
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

# 게임 플레이
playCount = 1
strikeOut = 0
while play:

    # 플레이어 리스트 생성 및 카운트 표출
    playerList = []
    print("시도횟수 : ",playCount)

    # • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
    print("정수 3개를 입력하세용~~^_^")
    while len(playerList) < 3:
        playerList.append(int(input()))
    
    # 스트라이크 볼 아웃 판별식
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
    # • 아래 경우 게임 Lose – Strike out == 2
    if strike == 0 and ball == 0:
        strikeOut += 1
        if strikeOut > 1:
            play=False
            print("2스트라이크 아웃! ㅠㅠ")
            print("아까비~~~졌네용..")
            print("정답은 : ",gameList," 입니다.")
            break
        else:
            print("Out : 아웃 1번")
    # • 아래 경우 게임 Win – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우
    elif strike == 3:
        play=False
        print("정답입니다~~^_^")
        print("정답은 : ",gameList," 입니다!")
        break
    else: # 정답이 아닌 경우에는 strike와 ball를 출력
        if strike > 0:
            print(strike, " Strike")
        if ball > 0:
            print(ball," Ball")
    # • 아래 경우 게임 Lose – 시도 횟수 >= 5
    playCount += 1
    if playCount > 4:
        play = False
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList," 입니다.")
        break