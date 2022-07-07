# 220706 주현 첨삭

def inputMenu():
    print("---------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("---------------")
inputMenu()

Menu = int(input("메뉴를 입력하세요."))

if Menu == 1:
    dan = int(input("알고 싶은 구구단을 입력하세요."))
    for dan_L in range(dan, dan+1):
        for dan_R in range(1, 10):
            if 9 >= dan >= 2:
                print(dan_L,"X",dan_R,"=",dan_L*dan_R )
                
            else:
                print("Error Msg")
                continue
        inputMenu()
        num = int(input(""))
        if num == 1:
            continue
        else:
            print("이용해주셔서 감사합니다.")
        
elif Menu == 2:
    print("이용해주셔서 감사합니다.")
else:
    print("Error Msg")