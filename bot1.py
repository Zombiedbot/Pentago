import random
import pentago

def do_turn2(M, s):
    summ = -10 ** 9
    for i in range(6):
        for j in range(6):
            sus1 = 0
            M1 = M[:]
            if M1[i][j] == '.':
                M1[i][j] = s
                for q in range(1, 5):
                    for d in range(2):
                        pentago.rotate(q, d, M1)
                        sus1 += check_5(M1, s)
                        sus1 += check_4(M1, s)
                        sus1 += check_3(M1, s)
                        sus1 += check_2(M1, s)
                        sus1 += check_1(M1, s)
                        sus1 += check_crest(M1, s)
                        if sus1 >= summ:
                            summ = sus1
                        d1 = (d + 1) % 2
                        pentago.rotate(q, d1, M1)
                M[i][j] = '.'
    return summ

def make_turn(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    summ = -10 ** 9
    '''xx = 2
    yy = 2
    qq = 1
    dd = 1'''
    for i in range(6):
        for j in range(6):
            sus1 = 0
            M1 = M[:]
            if M1[i][j] == '.':
                M1[i][j] = s
                M2 = M1[:]
                for q in range(1, 5):
                    for d in range(2):
                        sus1 = 0
                        pentago.rotate(q, d, M1)
                        sus1 += check_5(M1, s)
                        sus1 += check_4(M1, s)
                        sus1 += check_3(M1, s)
                        sus1 += check_2(M1, s)
                        sus1 += check_1(M1, s)
                        sus1 += check_crest(M1, s)
                        
                        sus1 -= check_5(M1, f)
                        sus1 -= check_4(M1, f)
                        sus1 -= check_3(M1, f)
                        sus1 -= check_2(M1, f)
                        sus1 -= check_1(M1, f)
                        sus1 -= check_crest(M1, f)
                        
                        #sus1 = sus1 - do_turn2(M1, f)
                        #print(sus1)
                        if sus1 >= summ:
                            xx = j
                            yy = i
                            qq = q
                            dd = d
                            summ = sus1
                        M1 = M2[:]
                M1[i][j] = '.'
    print(summ)
    return(xx + 1, yy + 1, qq, dd) 


def check_5(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    sus = 0
    for i in M:
        h = 0
        for j in range(6):
            if 0 < j < 5 and i[j] != s:
                break
            if i[j] == s:
                h += 1
        if h >= 5:
            sus += 10 ** 10
    h = 0
    for j in range(6):
        h = 0
        for i in range(6):
            if 0 < i < 5 and M[i][j] != s:
                break
            if M[i][j] == s:
                h += 1
        if h >= 5:
            sus += 10 ** 10
    h = 0
    for i in range(6):
        if 0 < i < 5 and M[i][i] != s:
            break
        if M[i][i] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0
    for i in range(6):
        if 0 < i < 5 and M[i][5 - i] != s:
            break
        if M[i][5 - i] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0
    for i in range(5):
        if M[i][4 - i] != s:
            break
        if M[i][4 - i] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0
    for i in range(1 , 6):
        if M[i][6 - i] != s:
            break
        if M[i][6 - i] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0
    for i in range(5):
        if M[i][i + 1] != s:
            break
        if M[i][i + 1] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0
    for i in range(1 , 6):
        if M[i][i - 1] != s:
            break
        if M[i][i - 1] == s:
            h += 1
    if h >= 5:
        sus += 10 ** 10
    h = 0

    return sus
    
def check_4(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    sus = 0
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] == '.':
                    b += 1
                else:
                    b = 0
            else:
                if M[i][j] == s:
                    b += 1
                else:
                    b = 0
        if b == 6:
            sus += 10 ** 8
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[j][i] == '.':
                    b += 1
                else:
                    b = 0
            else:
                if M[j][i] == s:
                    b += 1
                else:
                    b = 0
        if b == 6:
            sus += 10 ** 8
    b = 0
    for i in range(6):
        b = 0
        if i == 0 or i == 5:
            if M[i][i] == '.':
                b += 1
            else:
                b = 0
        else:
            if M[i][i] == s:
                b += 1
            else:
                b = 0
    if b == 6:
        sus += 10 ** 8
    b = 0
    for i in range(6):
        b = 0
        if i == 0 or i == 5:
            if M[i][5 - i] == '.':
                b += 1
            else:
                b = 0
        else:
            if M[i][5 - i] == s:
                b += 1
            else:
                b = 0
    if b == 6:
        sus += 10 ** 8
    return sus

def check_3(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    sus = 0
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] != '.':
                    break
            else:
                if M[i][j] == s:
                    b += 1
                elif M[i][j] != '.':
                    break
        if b == 3:
            sus += 10 ** 6
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[j][i] != '.':
                    break
            else:
                if M[j][i] == s:
                    b += 1
                elif M[j][i] != '.':
                    break
        if b == 3:
            sus += 10 ** 6
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][i] != '.':
                break
        else:
            if M[i][i] == s:
                b += 1
            elif M[i][i] != '.':
                break
    if b == 3:
        sus += 10 ** 6
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][5 - i] != '.':
                break
        else:
            if M[i][5 - i] == s:
                b += 1
            elif M[i][5 - i] != '.':
                break
    if b == 3:
        sus += 10 ** 6
    return sus

def check_2(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    sus = 0
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] != '.':
                    break
            else:
                if M[i][j] == s:
                    b += 1
                elif M[i][j] != '.':
                    break
        if b == 2:
            sus += 10 ** 4
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[j][i] != '.':
                    break
            else:
                if M[j][i] == s:
                    b += 1
                elif M[j][i] != '.':
                    break
        if b == 2:
            sus += 10 ** 4
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][i] != '.':
                break
        else:
            if M[i][i] == s:
                b += 1
            elif M[i][i] != '.':
                break
    if b == 2:
        sus += 10 ** 4
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][5 - i] != '.':
                break
        else:
            if M[i][5 - i] == s:
                b += 1
            elif M[i][5 - i] != '.':
                break
    if b == 2:
        sus += 10 ** 4
    return sus

def check_1(M, s):
    if s == 'X':
        f = 'O'
    else:
        f = 'X'
    sus = 0
    for i in range(6):
        b = 0
        for j in range(6):
            if j == 0 or j == 5:
                if M[i][j] != '.':
                    break
            else:
                if M[i][j] == s:
                    b += 1
                elif M[i][j] != '.':
                    break
        if b == 1:
            sus += 10 ** 2
    for i in range(6):
        b = 0
        for j in range(6):
            if i == 0 or i == 5:
                if M[j][i] != '.':
                    break
            else:
                if M[j][i] == s:
                    b += 1
                elif M[j][i] != '.':
                    break
        if b == 1:
            sus += 10 ** 2
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][i] != '.':
                break
        else:
            if M[i][i] == s:
                b += 1
            elif M[i][i] != '.':
                break
    if b == 1:
        sus += 10 ** 2
    b = 0
    for i in range(6):
        
        if i == 0 or i == 5:
            if M[i][5 - i] != '.':
                break
        else:
            if M[i][5 - i] == s:
                b += 1
            elif M[i][5 - i] != '.':
                break
    if b == 1:
        sus += 10 ** 2
    return sus

def check_crest(M, s):
    sus = 0
    if M[0][1] == M[1][0] == M[1][1] == M[1][2] == M[2][1] == s:
        if M[1][4] == s and M[0][4] == M[2][4] == '.':
            sus += 10 ** 10
        if M[4][1] == s and M[4][0] == M[4][2] == '.':
            sus += 10 ** 10
    if M[3][1] == M[4][0] == M[4][1] == M[4][2] == M[5][1] == s:
        if M[4][4] == s and M[3][4] == M[5][4] == '.':
            sus += 10 ** 10
        if M[1][1] == s and M[1][0] == M[1][2] == '.':
            sus += 10 ** 10
    if M[3][4] == M[4][3] == M[4][4] == M[4][5] == M[5][4] == s:
        if M[4][1] == s and M[3][1] == M[5][1] == '.':
            sus += 10 ** 10
        if M[1][4] == s and M[1][3] == M[1][5] == '.':
            sus += 10 ** 10
    if M[0][4] == M[1][3] == M[1][4] == M[1][5] == M[2][4] == s:
        if M[1][1] == s and M[0][1] == M[2][1] == '.':
            sus += 10 ** 10
        if M[4][4] == s and M[4][3] == M[4][5] == '.':
            sus += 10 ** 10
    return sus
