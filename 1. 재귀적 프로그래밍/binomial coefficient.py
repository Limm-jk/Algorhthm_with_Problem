# /**
#  * @author [Limm-jk]
#  * @email [201602057@cs-cnu.org]
#  * @create date 2020-11-06 19:41:45
#  * @modify date 2020-11-06 19:41:45
#  * @desc [이항계수]
#  */

def compose(n, r):
    if r == 0 or n == r:
        return 1
    else:
        return compose(n-1, r-1) + compose(n-1, r)

n, r = input('input n, r : ').split()
n = int(n)
r = int(r)

print(compose(n,r))