from aocd import get_data
from aocd import submit

sample = open("sample.txt", "r").read()
answer = open("output.txt", "r").read()

act = int(answer) if answer.isnumeric() else -69

cb = 0


def comp(a):
    global cb
    return ord(a[cb])


def solve(data):
    board = [x for x in data.split('\n')]
    gamma = ""
    beta = "0"
    global cb
    left = 0
    right = len(board) - 1

    while left < right:
        board = board[:left] + sorted(board[left:right + 1], key=comp) + board[right + 1:]
        mid = (left + right + 1) // 2
        if (right-left)%2 == 1 and board[mid][cb] == '1' and board[mid-1][cb] == '0':
            print("mooooo", cb)
            left = mid
        elif board[mid][cb] == '0':
            for i in range(mid, right + 1):
                if board[i][cb] == '1':
                    right = i - 1
                    break
        else:
            for i in range(left, mid + 1):
                if board[i][cb] == '1':
                    left = i
                    break

        for i in board:
            print(i)
        print(left, right, cb, end = '\n\n')
        cb += 1

    gamma = board[left]
    left = 0
    right = len(board) - 1
    cb = 0

    while left < right:
        board = board[:left] + sorted(board[left : right + 1], key=comp) + board[right + 1:]
        mid = (left + right + 1) // 2
        if (right-left) % 2 == 1 and board[mid][cb] == '1' and board[mid-1][cb] == '0':
            print("mooo", cb)
            right = mid-1
        elif board[mid][cb] == '0':
            for i in range(mid, right + 1):
                if board[i][cb] == '1':
                    left = i
                    break
        else:
            for i in range(left, mid + 1):
                if board[i][cb] == '1':
                    right = i - 1
                    break
        for i in board:
            print(i)
        print(left, right, cb, end = '\n\n')
        cb += 1
    cb = 0
    beta = board[left]
    print(gamma, beta)
    return int(gamma, 2) * int(beta, 2)


def answer():
    if sample == "" or act == -69:
        submit(solve(get_data(day=3, year=2021)), day=3, year=2021)
        return
    expected = solve(sample)
    if expected == act:
        submit(solve(get_data(day=3, year=2021)), day=3, year=2021)
    else:
        print("Wrong answer!!")
        print("Your answer:", expected)
        print("Actual answer: ", act)


answer()
