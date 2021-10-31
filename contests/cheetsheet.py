# 入出力
import itertools
x, y = map(int, input().split())
# 1行・複数列
x = list(map(int, input().split()))
# 複数行・一列
x = [list(map(int, input().split())) for i in range(n)]


# 組み合わせ
all_list = list(itertools.permutations(num_list))
