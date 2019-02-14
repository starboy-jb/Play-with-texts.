import sys
sys.setrecursionlimit(4800)

mx = int(1e9 + 1)
mp = dict()


def check(n, m, flag):
    if m == 0:
        return 0
    if n == 0:
        return mx
    tp = str(n) + str(m) + str(flag)
    if tp in mp.keys():
        return mp[tp]
    if str1[n - 1] == str2[m - 1]:
        if flag == 0:
            mp[tp] = min(check(n - 1, m - 1, 1), check(n - 1, m, 0))
            return mp[tp]
        else:
            mp[tp] = check(n - 1, m - 1, 1)
            return mp[tp]
    if flag == 0:
        mp[tp] = check(n - 1, m, 0)
        return mp[tp]
    mp[tp] = 1 + check(n - 1, m, 1)
    return mp[tp]


for _ in range(int(input())):
    str1 = input()
    str2 = input()
    n = len(str1)
    m = len(str2)
    ans = check(n, m, 0)
    mp.clear()
    if ans < n:
        print('Yes')
        print(ans)
    else:
        print('No')
