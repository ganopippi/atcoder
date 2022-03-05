# 競プロ用チートシート
## 目次
- [競プロ用チートシート](#競プロ用チートシート)
  - [目次](#目次)
  - [入出力](#入出力)
    - [1行・複数列](#1行複数列)
      - [複数の変数](#複数の変数)
      - [リストに整数を格納する](#リストに整数を格納する)
    - [複数行・一列](#複数行一列)
    - [複数行・複数列](#複数行複数列)
    - [1文字ずつlist](#1文字ずつlist)
  - [配列](#配列)
    - [配列の1次元へのコピー](#配列の1次元へのコピー)
    - [縦横入れ替え](#縦横入れ替え)
  - [ライブラリ](#ライブラリ)
    - [itertools](#itertools)
      - [全通りの組み合わせ](#全通りの組み合わせ)
    - [dataframe](#dataframe)
      - [dfのカラムの型確認](#dfのカラムの型確認)
      - [各カラム間の相関係数の産出](#各カラム間の相関係数の産出)
    - [numpy](#numpy)
      - [リストの行を増やす方向への連結](#リストの行を増やす方向への連結)
    - [matplotlib](#matplotlib)
      - [グラフの表示系](#グラフの表示系)
  - [その他](#その他)
    - [ゼロ埋め](#ゼロ埋め)
  - [todo](#todo)
## 入出力
### 1行・複数列
#### 複数の変数
```python
x, y = map(int, input().split())
```
#### リストに整数を格納する
```python
x = list(map(int, input().split()))
```
### 複数行・一列
```python
# 文字列
x = [input() for i in range(5)]
# 数値
x = [int(input()) for i in range(rows)]
```
### 複数行・複数列
```python
x = [list(map(int, input().split())) for i in range(n)]
```
### 1文字ずつlist
```python
s = list(input())
```
## 配列
### 配列の1次元へのコピー
```python
a = [[0,1],[2,3]] # どちらにしろ [0,1,2,3]と1次元になる
b = a.ravel() # 参照を返す
c = a.flatten() # copyを返す
```
### 縦横入れ替え
```python
res = [list(x) for x in zip(*list_name)]
```
## ライブラリ
### itertools
#### 全通りの組み合わせ
```python
all_list = list(itertools.permutations(num_list))
```
### dataframe
#### dfのカラムの型確認
```python
df.dtypes
```
#### 各カラム間の相関係数の産出
`df.corr()`
### numpy
#### リストの行を増やす方向への連結
`np.vstack([a,b])`

```python
a = np.array([[0,1,10],[0,1,10]])
b = np.array([100,100,100])
np.vstack([a,b]) 
# 出力結果
array([[ 0, 1, 10], [ 0, 1, 10], [100, 100, 100]])
```

### matplotlib
#### グラフの表示系
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(ncols=2)

axes[0].set_title("graph left") #サブタイトル
axes[1].set_title("graph right") #サブタイトル
fig.suptitle("fig title") #タイトル設定
plt.show()
```

## その他
### ゼロ埋め
```python
n.zfill(4) 
```
## todo
- 複数行・複数列