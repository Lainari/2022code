# • 게임 시작 시 0~9사이 정수 중 중복 값이 없는 난수 3개 생성
import random

gameList =[]
while len(gameList) < 3:
    # 난수 생성
    check = random.randint(0,9)
    # 난수 생성 값이 게임 리스트에 없을 경우 추가, 아니면 재생성
    if check not in gameList:
        gameList.append(check)

# 변수 생성
strikeOut = 0
playCount = 1

# • 키보드로부터 0~9사이 정수 3개를 입력 받고 결과 값을 출력 (예외처리 X)
while True: # 게임은 특정한 상황이 아닌 경우 지속 실행
    print("시도횟수 : ",playCount)
    print("정수 3개를 입력하세용~~~^_^")
    playerList=[]

    # 플레이어 리스트 원소가 3개가 될 때까지 입력받기
    while len(playerList) < 3:
        playerList.append(int(input()))

    # 변수생성
    strike = 0
    ball = 0

    # 플레이어 리스트 원소들이 게임 리스트에 속하는지 판별
    for value in range(3):
        if playerList[value] in gameList:
            # 있다면 스트라이크, 아니라면 볼을 판별
            if playerList[value] == gameList[value]:
                strike += 1
            else:
                ball += 1
        # 리스트에 속하지 않은 원소라면 다음 원소로 넘겨서 그 원소또한 속하는지 판별하게끔 만들기
        else:
            continue

    # 반복문이 끝나고 strike 와 ball 이 각각 0이라면 Out 이므로 해당 값을 증가시킨다
    if strike == 0 and ball == 0:
        strikeOut += 1
        # 만일, 증가한 값이 2 라면 break, 아니라면 Out : 아웃 1번을 출력한다
        if strikeOut == 2:
            print("스트라이크 아웃 2회! ㅠㅠ")
            print("아까비~~~졌네용")
            print("정답은 : ",gameList,"입니다")
            break
        else:
            print("Out : 아웃 1번")
            
    # 반복문이 끝나고 strike 값이 3회라면 모든 정답을 맞췄으므로 성공 msg와 탈출
    else:
        if strike == 3:
            print("성공~!!")
            print("정답은 : ",gameList,"입니다.")
            break
        # 아니면 strike 값과 ball 값에 따라 msg 표출
        else:
            if strike > 0:
                print(strike," Strike",end=" ")
            if ball > 0:
                print(ball," Ball",end=" ")
            print()

    # 해당 검사를 마치고 playCount를 증가시키고, 해당 값이 일정 값이 넘으면 break
    playCount += 1
    if playCount >= 5:
        print("게임횟수 초과")
        print("아까비~~~졌네용")
        print("정답은 : ",gameList,"입니다")
        break