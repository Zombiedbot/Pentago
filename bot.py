def dfs1(M, i, j, H, V, D1, D2, s):
    if i < 5:
        dfs1(M, i + 1, j, H, V, D1, D2, s)
        if M[i][j] != '.':
            if M[i + 1][j] == M[i][j]:
                V[i][j] = V[i][j + 1] * 10
            else:
                V[i][j] = 1
    else:
        if M[i][j] == s:
            V[i][j] = 1
        elif M[i][j] != '.':
            V[i][j] = -1
    if j < 5:
        dfs1(M, i, j + 1, H, V, D1, D2, s)
        if M[i][j] != '.':
            if M[i][j + 1] == M[i][j]:
                H[i][j] = H[i][j + 1] * 10
            else:
                H[i][j] = 1
    else:
        if M[i][j] == s:
            H[i][j] = 1
        elif M[i][j] != '.':
            H[i][j] = -1
    if j < 5 and i < 5:
        dfs1(M, i, j + 1, H, V, D1, D2, s)
        if M[i][j] != '.':
           if M[i + 1][j + 1] == M[i][j]:
                D1[i][j] = D1[i + 1][j + 1] * 10
           else:
                D1[i][j] = 1 
    
def step(M):
    H = [[0 for i in range(6)] for j in range(6)]
    V = [[0 for i in range(6)] for j in range(6)]
    D1 = [[0 for i in range(6)] for j in range(6)]
    D2 = [[0 for i in range(6)] for j in range(6)]
    M1 = M[:]
    
