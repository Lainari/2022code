def play(a,b,c):
# 승리 : strike >= 3
    if a == 3:
        print("삼진")
# 패배 1 : strikeOut >= 2
    if b == 2:
        print("아웃 2번 끝")
# 패배 2 : playCount >= 5
    if c == 5:
        print("게임 횟수 초과")

# 0 ~ 9 까지 난수 생성, 중복값 X
import random

gameList = []
while len(gameList) < 3:
    check = random.randint(0,9)
    if check not in gameList:
        gameList.append(check)

playCount = 1
strikeOut = 0
# 사용자에게 키보드로부터 3가지의 값을 입력 받기
while True:
    print(gameList)
    print("시도 횟수 : ",playCount)
    playerList=[]
    for value in range(3):
        playerList.append(int(input("정수를 입력해주세요 : ")))
    a=0
    strike = 0
    ball = 0
# 스트라이크, 볼 판정
    for value in range(3):
        if playerList[value] in gameList:
            if playerList[value] == gameList[value]:
                strike += 1
            else:
                ball += 1
    if strike == 0 and ball == 0:
        strikeOut += 1
    else:
        print(strike," Strike",ball," Ball")
    playCount += 1
    if strike >= 3 or strikeOut >=2 or playCount>=5:
        break
play(strike,strikeOut,playCount)
    
# # 승리 : strike >= 3
#     if strike >= 3:
#         break
# # 패배 1 : strikeOut >= 2
#     if strikeOut >= 2:
#         break
# # 패배 2 : playCount >= 5
#     playCount += 1
#     if playCount >= 5:
#         break