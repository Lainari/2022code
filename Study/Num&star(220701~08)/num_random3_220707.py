# 1 ~ 10 사이 난수 5개를 List에 저장 후
# 난수 값을 출력하라.

# 난수 함수 사용, List 사용
import random
myList=[]
# 1 ~ 10개 사이 난수 5개를 List에 저장
for value in range(5):
    myList.append(int(random.random()*10)+1)
# 난수 값을 출력
    print(myList[value])