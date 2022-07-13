# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random

# 난수 리스트 생성
gameList = []

# 난수 3개 생성할 동안 중복값 판별
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)

# 게임이 특정 조건을 만족하기 전에는 계속 실행
strikeOut = 0
playCount = 0

while True:

    # 게임횟수를 증가 시키고 조건 값보다 높으면 게임은 종료된다
    playCount += 1
    if playCount >= 5:
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList,"입니다")
        break

    # 키보드로부터 정수 3개 입력받기
    playerList=[]
    print("시도횟수 : ",playCount)
    print("정수 3개를 입력해주세용~~~^_^")
    while len(playerList)< 3:
        playerList.append(int(input()))

    # 플레이어와 게임 리스트가 모두 준비되었으므로 볼, 스트라이크, 스트라이크 아웃 판별식 작성
    strike = 0
    ball = 0

    for value in range(3):
        # 게임리스트 안에 해당 값이 있는지 판별
        if playerList[value] in gameList: 
            # 있으면 그 값이 동일한 위치에 있는지 판별
            if playerList[value] == gameList[value]:
                strike += 1
            # 아니면 볼
            else:
                ball += 1
        # 해당 값이 없으면 다음 순번으로 넘어가기

    # 스트라이크가 만약 3회라면 게임은 종료된다, 아니면 strike 값과 ball 값을 표출
    if strike == 3:
        print("승리~!!! *^o^* ")
        print("정답   : ",gameList)
        print("입력값 : ",playerList)
        break

    # 만일 둘다 0인 경우 (전 원소 불일치) 아웃 카운트 증가
    elif strike == 0 and ball == 0:
        strikeOut += 1

        # 증가한 Out 카운트가 2 이상이라면 게임은 종료 된다
        if strikeOut >= 2:
            print("2스트라이크 아웃입니다! ㅠㅠ")
            print("아까비~~~졌네용..")
            print("정답은 : ",gameList,"입니다")
            break

        # 아닐 경우 Out 카운트가 1번밖에 안났으므로 해당msg 출력
        print("Out : 아웃 1번")

    # strike 값과 ball 값에 따라 표출하는 msg
    else:
        if strike > 0:
            print(strike," Strike",end=" ")
        if ball > 0:
            print(ball," Ball",end=" ")
        print()

    # strike, ball, strikeOut 판별식 종료 후 해당 조건이 해당되지 않는다면 다시 게임 초기 상태로 돌아간다