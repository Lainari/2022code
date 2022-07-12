# 난수 함수 호출
import random

# 난수 리스트 생성
gameList=[]

# 중복되지 않는 3개의 난수
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

# 변수 생성
playCount = 0
strikeOut = 0

# 게임 시작
while True:

    playCount += 1
    # 시도횟수가 5회에 다다르거나 2 아웃이 되면 게임은 종료된다
    if playCount >= 5:
        print("게임횟수 초과")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList,"입니다.")
        break
    elif strikeOut >= 2:
        print("2 아웃...ㅠㅠ")
        print("아까비~~~졌네용..")
        print("정답은 : ",gameList,"입니다.")
        break

    print("시도횟수 : ",playCount)
    # 사용자 입력 리스트 생성
    playerList = []
    print("정수 3개를 입력하세용~~~^_^")
    # 사용자 입력
    while len(playerList) < 3:
        playerList.append(int(input()))
    
    # 변수 생성
    strike = 0
    ball = 0

    # 사용자 입력값과 난수값 비교
    for value in range(3):
        if playerList[value] in gameList:
            if playerList[value] == gameList[value]:
                strike += 1
            else:
                ball += 1
    
    # strike 값에 따른 판별식
    if strike == 3:
        print("삼진~~*^_^*")
        print("정답은 : ",gameList,"입니다.")
        print("입력값 : ",playerList,"입니다.")
        break

    # 만약 둘다 0일 경우는 strikeOut 값을 증가 시킨다
    elif strike == 0 and ball == 0:
        strikeOut += 1

    # 그외의 경우엔 해당 값에 따른 msg 출력
    else:
        if strike > 0:
            print(strike," Strike",end=" ")
        if ball > 0:
            print(ball," Ball",end=" ")
    print()