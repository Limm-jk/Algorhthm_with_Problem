# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-11-07 16:01:53
#  * @modify date 2020-11-07 16:01:53
#  * @desc [피보나치]
#  */

def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

# 이와 같은 방식은 중복계산이 많아서 시간이 오래걸림.
# 이 방법을 해결하기 위하여 메모이제이션 방식 채택
memo = [0 for i in range(200)]
def fibo2(n):
    if memo[n] != 0:
        return memo[n]

    if n == 1 or n == 2:
        memo[n] = 1
        return memo[n]
    else:
        memo[n] = fibo2(n-1) + fibo2(n-2)
        return memo[n]


n = int(input())

print(fibo2(n))

