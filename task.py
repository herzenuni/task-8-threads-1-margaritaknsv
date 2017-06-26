import threading

X = [[2, 4], [1, 2]]
Y = [[5, 2], [2, 7]]

def calculate_element(row, col):
    result = 0
    for i, item in enumerate(row):
        result += item * col[i]
    return result

def calculate_row(rowX, Y):
    cols = [[row[i] for row in Y] for i in range(len(Y[0]))]
    result = list(map(lambda x: calculate_element(rowX, x), cols))
    print(result)
    return result

for row in X:
    threading.Thread(target=calculate_row, args=(row, Y)).start()
