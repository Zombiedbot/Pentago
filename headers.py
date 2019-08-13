def correct(x, y, q, d, M):
    try:
        assert (x<=6 and x>=1 and y<=6 and y>=1)
    except AssertionError:
        print('Wrong coordinates. Write another data: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        return correct(x, y, q, d, M)
    try:
        assert M[y-1][x-1]=='.'
    except AssertionError:
        print('This point is occupied. Write another data: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        return correct(x, y, q, d, M)
    try:
        assert q>=1 and q<=4
    except AssertionError:
        print('Wrong quater. Write another data: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        return correct(x, y, q, d, M)
    try:
        assert d==1 or d==0
    except AssertionError:
        print('Wrong direction. Write another data: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        return correct(x, y, q, d, M)
    return (x, y, q, d)

def check(s, M):
    h=0
    for i in M:
        h = 0
        for j in i:
            if j==s:
                h+=1
            else:
                h=0
            if h==5:
                return 1
    h=0
    for i in range(6):
        h = 0
        for j in range(6):
            if M[j][i]==s:
                h+=1
            else:
                h=0
            if h==5:
                return 1
    h=0
    for i in range(6):
        if M[i][i]==s:
            h+=1
        else:
            h=0
        if h==5:
            return 1
    h=0
    for i in range(6):
        if M[5-i][i]==s:
            h+=1
        else:
            h=0
        if h==5:
            return 1
    h1=0
    h2=0
    for i in range(5):
        if M[i][i+1]==s:
            h1+=1
        else:
            h1=0
        if h1==5:
            return 1
        
        if M[i+1][i]==s:
            h2+=1
        else:
            h2=0
        if h2==5:
            return 1
    h1=0
    h2=0
    for i in range(5):
        if M[5-i][i+1]==s:
            h1+=1
        else:
            h1=0
        if h1==5:
            return 1
        if M[4-i][i]==s:
            h2+=1
        else:
            h2=0
        if h2==5:
            return 1
    
