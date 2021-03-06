#  1) 키보드로부터 정수 값 입력
#  2) “1” 이상의 값만 입력, “0” 이하의 값 입력 시 "1 이상 양수를 출력해주세요" Msg 출력 후 재입력
#  3) 현재 입력 횟수 출력 후 키보드 입력 값 화면에 출력
#  4) “짝수”or “양수” 출력
#  5) 3의 배수 또는 7의 배수이면 아래 Msg 출력
#  6) ‘20,000’ 입력 시 아래 Msg 출력 후 프로그램 종료
#  7) 출력 값은 반드시 아래 형식 준수

# 0. 정수값 입력 받기랑 입력 횟수 저장 공간 생성
input_value = 0
count = 1

# 1. 반복문 생성(2만이 아닌경우 계속 실행)
while input_value != 20000:
    # 2. 값 입력
    input_value=int(input())
    # 3. 만약 입력 값이 20000 이라면 break
    if input_value==20000:
        break
    # 4. 아닐 경우 아래 패턴 출력
    else:
        # 5. 만약 0 이하의 값을 입력했을때
        if input_value <= 0:
            # 6. 해당 구문 출력 후 continue 하여 while문 재실행
            print("1 이상 양수를 출력해주세요")
            continue
        # 6. 아닐 경우 전부 1이상 양수이므로 아래 패턴을 따라간다
        else:
            # 7. 만일 입력한 값이 짝수라면
            if input_value % 2 == 0:
                # 8. 입력값이 몇번쨰인지와 입력값을 출력하고
                print(count,"번째 입력값은 = ",input_value)
                # 9. 짝수를 출력한 뒤
                print("\t짝수 입니다.")
                # 10. 해당값이 3의 배수이거나 7의 배수이라면 해당 배수임을 출력하라
                if input_value % 3 == 0:
                    print("\t3의 배수입니다.")
                elif input_value % 7 == 0:
                    print("\t7의 배수입니다.")
                # 11. 해당 구문 종료 시 count 값을 증가시켜 번째를 늘려라
                count +=1
            # 12. 입력한 값이 홀수라면
            else:
                # 13. 입력값이 몇번쨰인지와 입력값을 출력하고
                print(count,"번째 입력값은 = ",input_value)
                # 14. 홀수를 출력하고
                print("\t홀수 입니다.")
                # 15. 해당값이 3의 배수이거나 7의 배수이라면 해당 배수임을 출력하라
                if input_value % 3 == 0:
                    print("\t3의 배수입니다.")
                elif input_value % 7 == 0:
                    print("\t7의 배수입니다.")
                # 16. 해당 구문 종료 시 count 값을 증가시켜 번째를 늘려라
                count +=1
# 17. 해당 while 문을 break 했다면 아래 MSG를 출력하고 프로그램 종료
print("이용해주셔서 감사합니다.")