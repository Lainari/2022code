 # 1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
import random
randomList=[]
for value in range(20):
    randomList.append(random.randint(1,20))
 # 2. List 내 원소 값에 대한 합계, 평균, 최대 값, 최소 값 출력
 # 3. List 내 중복 값과 중복 횟수 정보 출력
 # 4. 구간 별 히스토그램 정보 출력