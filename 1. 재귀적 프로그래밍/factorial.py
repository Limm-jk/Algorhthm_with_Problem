# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-11-04 13:53:00
#  * @modify date 2020-11-04 13:53:00
#  * @desc [1-1 팩토리얼]
#  */

# code 1-1
def factorial(n:int):
    r = 1
    for i in range(2,n+1):
        r *= i
    return r

# print(factorial(3))

# 생각해보기. 
# n의 값이 커지면 잘못된 결과 반환함. 왜?
# 아마 오버플로우...? 하지만 파이썬은 알아서 float로 바꿔준다구.

# code 1-2
def factorial2(n:int):
    if n == 1:
        return 1
    else:
        return n * factorial2(n-1)

# n의 값이 커지면 세그먼트 폴트가 발생함.
# 이는 재귀가 계속되다가 스택을 다 써버려서 스택오버플로우가 발생하기 때문.
# 파이썬은 이 외에도 재귀에 재귀 제한이 있다.
# 이는
# import sys
# sys.setrecursionlimit(10**6)
# 로 해결 가능