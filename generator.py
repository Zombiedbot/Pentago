import random
import pentago

def make_4_1():
    M = [['.' for i in range(6)] for i in range(6)]
    k = random.randint(1, 14)
    if k < 7:
        for i in range(1, 5):
            M[k - 1][i] = 'X'
        b = random.randint(5, 7)
        #print(b, k, 0)
        for i in range(b):
            c = 36 - 4 - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != k - 1:
                        d = d - 1
                    if not d and i != k - 1:
                        M[i][j] = 'O'
                        break
                        
        for i in range(b - 3):
            c = 36 - 3 - b - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != k - 1:
                        d = d - 1
                        if not d and i != k - 1:
                            M[i][j] = 'X'
                            break
        t = random.randint(1, 4)
        M[k - 1][t] = '.'
        if k < 4:
            if t < 3:
                q = 2
            else:
                q = 1
        else:
            if t < 3:
                q = 3
            else:
                q = 4
        d = random.randint(0, 1)
        pentago.rotate(q, d, M)

        
    elif 13 > k > 6:
        k = k - 6
        for i in range(1, 5):
            M[i][k - 1] = 'X'
        b = random.randint(5, 7)
        print(b, k, 1)
        for i in range(b):
            c = 36 - 4 - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and j != k - 1:
                        d = d - 1
                    if not d and j != k - 1:
                        M[i][j] = 'O'
                        break
                        
        for i in range(b - 3):
            c = 36 - 3 - b - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and j != k - 1:
                        d = d - 1
                        if not d and j != k - 1:
                            M[i][j] = 'X'
                            break
        t = random.randint(1, 4)
        M[t][k - 1] = '.'
        if k < 4:
            if t < 3:
                q = 2
            else:
                q = 3
        else:
            if t < 3:
                q = 1
            else:
                q = 4
        d = random.randint(0, 1)
        pentago.rotate(q, d, M)
    elif k == 13:
        for i in range(1, 5):
            M[i][i] = 'X'
        b = random.randint(5, 7)
        print(b, k, 1)
        for i in range(b):
            c = 36 - 4 - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != j:
                        d = d - 1
                    if not d and j != i:
                        M[i][j] = 'O'
                        break
                        
        for i in range(b - 3):
            c = 36 - 3 - b - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != j:
                        d = d - 1
                        if not d and i != j:
                            M[i][j] = 'X'
                            break
        t = random.randint(1, 4)
        M[t][t] = '.'
        if t < 3:
            q = 2
        else:
            q = 4
        d = random.randint(0, 1)
        pentago.rotate(q, d, M)
    else:
        for i in range(1, 5):
            M[i][5 - i] = 'X'
        b = random.randint(5, 7)
        print(b, k, 1)
        for i in range(b):
            c = 36 - 4 - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != 5 - j:
                        d = d - 1
                    if not d and i != 5 - j:
                        M[i][j] = 'O'
                        break
                        
        for i in range(b - 3):
            c = 36 - 3 - b - i - 2
            d = random.randint(1, c)
            for i in range(6):
                for j in range(6):
                    if M[i][j]=='.' and i != 5 - j:
                        d = d - 1
                        if not d and i != 5 - j:
                            M[i][j] = 'X'
                            break
        t = random.randint(1, 4)
        M[t][5 - t] = '.'
        if t < 3:
            q = 1
        else:
            q = 3
        d = random.randint(0, 1)
        pentago.rotate(q, d, M)
    aa = 0
    bb = 0
    for i in M:
        for j in i:
            if j == 'X':
                aa += 1
            elif j == 'O':
                bb += 1
    if aa != bb:
        return make_4_1()
    else:
        return M, b

def make_4_2():
    M, b = make_4_1()
    for i in range(6):
        for j in range(6):
            print(M[i][j], end='')
        print('')
    g = random.randint(1, b - 1)
    print(b)
    t = 0
    for i in range(6):
        for j in range(6):
            if M[i][j]=='O':
                g = g - 1
            if not g:
                M[i][j] = '.'
                x = j
                y = i
                t = 1
                break
        if t:
            break
    q = random.randint(1, 4)
    d = random.randint(0, 1)
    pentago.rotate(q, d, M)
    if d == 1:
        d = 0
    else:
        d = 1
    t = 0
    g = random.randint(1, b - 1)
    for i in range(6):
        for j in range(6):
            if M[i][j]=='X':
                g = g - 1
            if not g:
                M[i][j] = '.'
                t = 1
                break
        if t:
            break
    qq = random.randint(1, 4)
    dd = random.randint(0, 1)
    pentago.rotate(qq, dd, M)
    return M, x, y, q, b - 1

def make_3_1():
    M, *b = make_4_2()
    b = b[-1]
    q = random.randint(1, 4)
    d = random.randint(0, 1)
    pentago.rotate(q, d, M)
    return M, b

def make_3_2():
    M, b = make_3_1()
    g = random.randint(1, b - 1)
    t = 0
    for i in range(6):
        for j in range(6):
            if M[i][j]=='O':
                g = g - 1
            if not g:
                M[i][j] = '.'
                x = j
                y = i
                t = 1
                break
        if t:
            break
    q = random.randint(1, 4)
    d = random.randint(0, 1)
    pentago.rotate(q, d, M)
    if d == 1:
        d = 0
    else:
        d = 1
    t = 0
    g = random.randint(1, b - 1)
    for i in range(6):
        for j in range(6):
            if M[i][j]=='X':
                g = g - 1
            if not g:
                M[i][j] = '.'
                t = 1
                break
        if t:
            break
    qq = random.randint(1, 4)
    dd = random.randint(0, 1)
    pentago.rotate(qq, dd, M)
    return M, x, y, q, d

def check_4(M):
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] == '.':
                    b += 1
                else:
                    b = 0
            else:
                if M[i][j] == 'X':
                    b += 1
                else:
                    b = 0
        if b == 6:
            return True
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[j][i] == '.':
                    b += 1
                else:
                    b = 0
            else:
                if M[j][i] == 'X':
                    b += 1
                else:
                    b = 0
        if b == 6:
            return True
    b = 0
    for i in range(6):
        b = 0
        if i == 0 or i == 5:
            if M[i][i] == '.':
                b += 1
            else:
                b = 0
        else:
            if M[i][i] == 'X':
                b += 1
            else:
                b = 0
        if b == 6:
            return True
    b = 0
    for i in range(6):
        b = 0
        if i == 0 or i == 5:
            if M[i][5 - i] == '.':
                b += 1
            else:
                b = 0
        else:
            if M[i][5 - i] == 'X':
                b += 1
            else:
                b = 0
        if b == 6:
            return True
    return False

def check_3(M):
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] != '.':
                    break
            else:
                if M[i][j] == 'X':
                    b += 1
                elif M[i][j] != '.':
                    break
        if b == 3:
            return True
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[j][i] != '.':
                    break
            else:
                if M[j][i] == 'X':
                    b += 1
                elif M[j][i] != '.':
                    break
        if b == 3:
            return True
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][i] != '.':
                break
        else:
            if M[i][i] == 'X':
                b += 1
            elif M[i][i] != '.':
                break
        if b == 3:
            return True
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][5 - i] != '.':
                break
        else:
            if M[i][5 - i] == 'X':
                b += 1
            elif M[i][5 - i] != '.':
                break
        if b == 3:
            return True
    return False
    

if __name__ == '__main__':
    M, *b = make_3_2()            
    for i in range(6):
        for j in range(6):
            print(M[i][j], end='')
        print('')
    print(check_3(M))
