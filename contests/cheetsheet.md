# 競プロ用チートシート
## 目次
- [競プロ用チートシート](#競プロ用チートシート)
  - [目次](#目次)
  - [入出力](#入出力)
    - [1行・複数列](#1行複数列)
      - [複数の変数](#複数の変数)
      - [リストに整数を格納する](#リストに整数を格納する)
    - [複数行・一列](#複数行一列)
    - [1文字ずつlist](#1文字ずつlist)
  - [ライブラリ](#ライブラリ)
    - [itertools](#itertools)
      - [全通りの組み合わせ](#全通りの組み合わせ)
  - [その他](#その他)
    - [ゼロ埋め](#ゼロ埋め)
  - [todo](#todo)
## 入出力
### 1行・複数列
#### 複数の変数
```
x, y = map(int, input().split())
```
#### リストに整数を格納する
```
x = list(map(int, input().split()))
```
### 複数行・一列
```
x = [list(map(int, input().split())) for i in range(n)]
```
### 1文字ずつlist
```
s = list(input())
```
## ライブラリ
### itertools
#### 全通りの組み合わせ
```
import itertools
all_list = list(itertools.permutations(num_list))
```
## その他
### ゼロ埋め
```
n.zfill(4) 
```
## todo
- 複数行・複数列