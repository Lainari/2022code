# 메뉴 우선 출력 후 키보드로부터 정수 값 입력
play = True
while play:
    print("--------------------")
    print("1. 구구단 출력")
    print("2. 프로그램 종료")
    print("--------------------")
    inputValue = int(input())
# 메뉴에서 1 선택 시 구구단 출력, 2 선택 시 Msg 출력 후 프로그램 종료
    if inputValue == 1:
        while play:
            multiPlay=int(input("출력할 구구단을 입력해주세요.(2단 ~ 9단까지 지원) : "))
    #  “구구단 출력” 메뉴 선택 시 출력 할 단을 키보드로부터 입력
    #  출력 유효 단은 2 ~ 9
            if 1< multiPlay < 10:
                for value in range(1,9):
                    print(multiPlay, " X ", value, " = ", multiPlay*value)
                break
        #  2 ~ 9단 이외의 값이 들어올 경우 Error Msg. 출력 후 재입력
            else:
                print("2 ~ 9 사이 정수를 입력해주세요")
        # > 이외의 값 입력시 2~9사이 정수를 입력해주세요 출력
    elif inputValue == 2:
        break
# 메뉴에서 1 또는 2이외의 값이 입력될 경우 Error Msg 출력 후 재입력
    else:
        print("올바르지 않은 실행입니다. 다시 입력해주세요")
print("이용해주셔서 감사합니다.")