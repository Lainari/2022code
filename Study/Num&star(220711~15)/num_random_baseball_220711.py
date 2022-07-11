# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random
gameList=[]
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)
# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
playCount = 1
strikeOut = 0
while playCount < 5:
    print("시도횟수 : ",playCount)
    playerList=[]
    print("정수 3개를 입력하세용~~^_^")
    while len(playerList) < 3:
        playerList.append(int(input()))
    print()
# • 아래 경우 게임 Win – 컴퓨터에서 생성 한 난수 값을 자리 순서대로 맞출 경우
    if playerList == gameList:
        print("승리~!!~~!!")
        print("정답 : ",gameList)
        break
    # 정답을 맞추지 못해 스트라이크, 볼, 아웃의 판별
    strike = 0
    ball = 0
    for check in range(3):
        if playerList[check] == gameList[check]:
            strike += 1
        elif playerList[check] != gameList[check] and playerList[check] in gameList:
            ball += 1
    # 판별이 끝난 후 해당 값에 따른 출력문구
    if strike == 0 and ball == 0:
        strikeOut += 1
    if strike > 0:
        print(strike," strike",end=" ")
    if ball > 0:
        print(ball," ball",end="")
    if strikeOut > 0:
        print("Out : 아웃 1번")
    playCount += 1
    print()
# • 아래 경우 게임 Lose – 시도 횟수 >= 5 or – Strike out == 2
    if playCount >= 5:
        print()
        print("게임횟수 초과")
        print("아까비~~~ 졌네용..")
        print("정답은 : ",gameList,"입니다.")
    elif strikeOut == 2:
        print()
        print("2 스트라이크 아웃!!! ㅠㅠ")
        print("아까비~~~ 졌네용..")
        print("정답은 : ",gameList,"입니다.")