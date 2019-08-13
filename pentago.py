import headers
M=[['.' for i in range(6)] for i in range(6)]
def swap(a, b):
    buf=a
    a=b
    b=buf
    
def put(x, y, q, d, s, M):
    #x, y, q, d = headers.correct(x, y, q, d, M)
    M[y-1][x-1]=s

def rotate(q, d, M):
    v=3*((q-1)//2)
    h=3*(q==4 or q==1)
    L=[]
    for i in range(v, v+3):
        L.append(M[i][h:h+3])
    if d==1:
        for i in range(3):
            M[v+i][h]=L[2][i]
            M[v+i][h+1]=L[1][i]
            M[v+i][h+2]=L[0][i]
    else:
        for i in range(3):
            M[v+i][h]=L[0][2-i]
            M[v+i][h+1]=L[1][2-i]
            M[v+i][h+2]=L[2][2-i]

if __name__=='__main__':                   
    t=True
    for i in M:
        for j in i:
            print(j, end='')
        print('')
    for i in range(18):
        print('players A turn: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        put(x, y, q, d, 'X', M)
        rotate(q, d, M)
        for i in M:
            for j in i:
                print(j, end='')
            print('')
        if headers.check('X', M):
            print('palyer A win')
            t=False
            break
        print('players B turn: ', end='')
        x, y, q, d=(int(i) for i in input().split())
        put(x, y, q, d, 'O', M)
        rotate(q, d, M)
        for i in M:
            for j in i:
                print(j, end='')
            print('')
        if headers.check('O', M):
            print('palyer A win')
            t=False
            break
    if t:
        print('draw')
