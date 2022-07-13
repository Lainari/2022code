# 유효 주민등록번호 검사 알고리즘

# 체크수 고정
checkNum = "234567892345"

# 사용자로부터 주민번호 입력받기
userNum = input("주민번호 13자리를 입력하세요 : ")

# 주민등록번호와 체크수 계산
count = 0
sum = 0
for value in range(13):
    if userNum[value].isdigit():
        sum = sum + (int(userNum[value]) * int(checkNum[count]))
        count+=1

# sum 값에 따른 유효성 체크
check = 11-(sum % 11) % 10
if check == int(userNum[-1]):
    print("유효한 주민번호 입니다")
else:
    print("유효하지않은 주민번호 입니다")