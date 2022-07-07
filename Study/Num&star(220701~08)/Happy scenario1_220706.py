play = True
while play:
    # 메뉴 우선 출력 후 키보드로부터 정수 값 입력
    print("--------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("--------------------")
    playNumber = int(input())

    # 메뉴에서 1 선택 시 구구단 출력, 2 선택 시 Msg 출력 후 프로그램 종료
    if playNumber == 1:
    #  “구구단 출력” 메뉴 선택 시 출력 할 단을 키보드로부터 입력
    #  출력 유효 단은 2 ~ 9
        multiplyPlay = True
        while multiplyPlay:
            print("출력할 구구단의 단을 입력하세요. 구구단의 단은 2 ~ 9 사이 입력")
            multiply = int(input())
            #  2 ~ 9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
            # > 이외의 값 입력시 2~9사이 정수를 입력해주세요 출력
            if multiply > 9 or multiply < 2:
                print("2~9사이 정수를 입력해주세요")
                continue
            else:
                break
        for dan_row in range(9):
            print(multiply," X ",dan_row+1," = ", multiply * (dan_row+1))
    elif playNumber == 2:
        play = False
        print("이용해주셔서 감사합니다")
# 메뉴에서 1 또는 2이외의 값이 입력될 경우 Error Msg 출력 후 재입력
    else:
        print("잘못 입력하셨습니다. 다시 입력하세요.")
        continue