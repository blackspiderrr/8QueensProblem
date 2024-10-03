# homework1 of 'Fundamentals of AI': 8Queens_Problem
# 2151094 SongZhengfei
from draw import draw
global Q
Q = []
def PLACE_QUEEN(row, n):
    global index
    for col in range(n):
        if flag_col[col] == 0 and line_up[row + col] == 0 and line_down[row - col + n - 1] == 0:
            # 放置并标记
            place_q[row] = col
            flag_col[col] = 1
            line_up[row + col] = 1
            line_down[row - col + n - 1] = 1
            if row < n - 1:
                PLACE_QUEEN(row + 1, n)
            else:
                index += 1
                Q.append(place_q.copy()) #copy不能省略，Q元素全都会变成新的place_q
            # 标记清空
            flag_col[col] = 0
            line_up[row + col] = 0
            line_down[row - col + n - 1] = 0
    return Q
if __name__ == '__main__':
    n = 8
    index = 0
    place_q = [0 for i in range(n)]
    flag_col = [0 for i in range(n)]
    line_up = [0 for i in range(2 * n - 1)]
    line_down = [0 for i in range(2 * n - 1)]
    Q = PLACE_QUEEN(0, n) #存放每种摆放情况的二维数组
    m = int(index/15)+1
    for k in range(m):
        draw(Q, k, index)
    print('Result of Queens:')
    for i in range(index):
        print(Q[i])
    print("总共有{}种结果".format(index))
