# 모듈 불러오기
import mo1
print(mo1.add(3,4))
print(mo1.sub(4,2))

print()

# 다른 방법으로 같은 결과 도출
from mo1 import add
print(add(3,4))
from mo1 import sub
print(sub(4,2))

print()
import mo1 as add
import mo1 as sub
ex = add.add(3,4)
ex2 = sub.sub(4,2)
print(ex)
print(ex2)