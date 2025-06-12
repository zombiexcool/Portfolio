

def erreur_colone(mat):
    for i in range(len(mat)):
        if mat[i].count(1) == 3:
            return i 
        

mat = [[1,1,0],[1,1,1],[1,0,1]]
print(erreur_colone(mat))