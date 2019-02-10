K, A, B = map(int, input().split())


biscuits  = 1

if B - A > 2 and A <= K - 1:
    #最初にA枚までクッキーを増やす
    K -= A - 1
    biscuits += A - 1

    biscuits  += (B - A) * (K // 2)
    K -= (K // 2) * 2
    biscuits += K
else:
    biscuits  += K

print(biscuits)
