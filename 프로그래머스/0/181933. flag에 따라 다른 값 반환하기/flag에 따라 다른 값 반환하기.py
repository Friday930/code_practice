def solution(a, b, flag):
    answer = 0
    return a - b if flag == 0 else a + b

answer = solution(-4, -3, True)