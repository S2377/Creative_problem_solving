def nullifyRow(matrix,row): 
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
        
def nullifyCol(matrix,col):   
    for i in range(len(matrix)):
        matrix[i][col] = 0
                
def nullyfy_row_col(matrix):
    rowHas_0 = False
    colHas_0 = False
    
    # check if first row contains o
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0 :
            rowHas_0 = True
                    
    # check if first col contains o
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            colHas_0 = True
            
            
    # check rest of rows and column 
    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    # check if first row contains o
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0 :
            nullifyCol(matrix,i)
            
    # check if first col contains o
    for i in range(len(matrix)):
        if matrix[i][0] == 0 :
            nullifyRow(matrix,i)
            
    if rowHas_0:
        nullifyRow(matrix,0)    
    if colHas_0:
        nullifyCol(matrix,0)
        
    return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
a = nullyfy_row_col(matrix)
print(a)

                
    
    
    
        
        
    