

def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int, input().split()))

    pipe = deque([])
    pipesize = 0

    for i in range(n):
        current = a[i]
        if pipesize >= current - 1:
            # 消すか消さないか
            temp = deque([])
            for j in range(current-1):
                curr_pipe = pipe.popleft()
                temp.appendleft(curr_pipe)
                if curr_pipe != current:
                    # 違ったら元に戻して追加
                    pipe.extendleft(temp)
                    pipe.appendleft(current)
                    break
        # 追加処理
        else:
            pipe.appendleft(current)

        pipesize = len(pipe)
        print(pipesize)
    # print(pipe)


main()
