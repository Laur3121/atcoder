a = int(input())
b = []
c = []

# 入力を処理
for _ in range(a):
    left, right = input().split()
    b.append(left)
    c.append(int(right))

# 最小値のインデックスを取得
min_value = min(c)
n = c.index(min_value)  # 最小値が最初に現れるインデックス

# 最小値以降の b を出力
for i in range(n , a):
    print(b[i])

# 最小値までの b を出力
for i in range(0, n ):
    print(b[i])
