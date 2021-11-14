
M=[
    [0,0,9,3,1,0,5,2,0],
    [5,3,1,7,0,6,0,0,0],
    [0,2,7,4,0,0,0,0,0],

    [4,0,0,0,7,0,3,0,2],
    [0,0,0,8,0,0,0,0,6],
    [0,0,0,0,0,3,4,7,0],

    [0,0,0,0,5,0,0,0,0],
    [0,0,0,0,0,7,0,4,9],
    [0,7,4,0,0,0,6,0,1]
]

def verify(M):
    complete=True
    duplicates_lines=False
    duplicates_colums=False

    for i in range(0,9):
        L=[1,2,3,4,5,6,7,8,9]
        K=[1,2,3,4,5,6,7,8,9]
        for j in range(0,9):
            if M[i][j]==0:
                complete=False
            try:
                L.remove(M[i][j])
            except:
                duplicates_lines=True
            try:
                K.remove(M[j][i])
            except:
                duplicates_colums=True
    return complete,duplicates_lines,duplicates_colums
                


def first_fill_matrice(M):
    G=M.copy()
    for i in range(0,len(G)):
        for j in range(0,len(G[i])):
            if G[i][j]==0:
                G[i][j]=[0,[1,2,3,4,5,6,7,8,9]]
            else:
                G[i][j]=[G[i][j],[]]
    return G

def refresh_notes(G):
    for i in range(0,9):
        for j in range(0,9):
            #for each notes
            if G[i][j][0]==0:
                #lines
                for k in range(0,9):
                    #if their are a number
                    if G[i][k][0]!=0:
                        try:
                            G[i][j][1].remove(G[i][k][0])
                        except:
                            pass
                    if G[k][j][0]!=0:
                        try:
                            G[i][j][1].remove(G[k][j][0])
                        except:
                            pass
                #square
                square=i//3,j//3
                for a in range(3*square[0],3*square[0]+3):
                    for b in range(3*square[1],3*square[1]+3):
                        if G[a][b][0]!=0:
                            try:
                                G[i][j][1].remove(G[a][b][0])
                            except:
                                pass
    return G

def step_resolve(G):
    for i in range(0,9):
        for j in range(0,9):
            if G[i][j][0]==0:
                #the only one note in a case
                if len(G[i][j][1])==1:
                    G[i][j]=G[i][j][1][0],[]
                #the only one note of a number in a case
                c=case_solve(G,i,j)
                if c!=0:
                    G[i][j]=c,[]
            

def case_solve(G,i,j):
    square=i//3,j//3
    for k in range(0,len(G[i][j][1])):
        for a in range(3*square[0],3*square[0]+3):
            for b in range(3*square[1],3*square[1]+3):
                if G[i][j][1][k]==G[a][b][0]:
                    return 0
        return G[i][j][1][k]

