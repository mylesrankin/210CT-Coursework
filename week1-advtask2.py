'''
by @mylesrankin (github)


'''



w,h = 5,5
sparse = [[0 for x in range(w)] for y in range(h)]
sparse[0][0] = 3
sparse[0][3] = 7
sparse[1][0] = 5
sparse[1][4] = 6
sparse[2][2] = 1
sparse[4][4] = 2

def convertSparse(sparse):
    stForm = []
    y = -1
    print("SPARSE MATRIX: ")
    for i in sparse:
        print(i)
        y += 1
        x = -1
        for j in i:
            x += 1
            if j > 0:
                ''' print("value:",j,"x:",x,"y:", y) '''
                ''' Here you would enter the data into the stForm matrix '''
                stForm.append([x,y,j])
    print("CONVERTED TO SPARSE TRIPLET FORM: ")
    for i in stForm:
        print(i)

def addMatrices():
    pass

def subMatrices():
    pass

def multMatrices():
    pass

        
convertSparse()




            
