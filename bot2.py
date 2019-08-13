import random
def make_turn(M):
    s = 0
    for i in M:
        for j in i:
            if j != '.':
                s += 1
    r = random.randint(1, 36 - s)
    
    for i in range(6):
        for j in range(6):
            if M[i][j] == '.':
                r = r - 1
                if not r:
                    x = j + 1
                    y = i + 1
                    break
    q = random.randint(1, 4)
    r = random.randint(0, 1)
    return (x, y, q, r) 
