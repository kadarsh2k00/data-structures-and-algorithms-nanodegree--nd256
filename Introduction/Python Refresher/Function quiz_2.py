correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
# Define a function check_sudoku() here:
def check_sudoku(matrix):
     p=len(matrix)
     m=[]
     for i in range(p):
          m.append(i+1)
     for i in range(p):
          k=[]
          n=[]
          for j in range(p):
               if(matrix[i][j] not in m):
                    return False
               if(matrix[i][j] not in k):
                    k.append(matrix[i][j])
               if(matrix[j][i] not in n):
                    n.append(matrix[j][i])
          if(len(k)!=len(m) or len(n)!=len(m)):
               return False
   
     return True





    
    
print(check_sudoku(incorrect))
#>>> False

print(check_sudoku(correct))
#>>> True

print(check_sudoku(incorrect2))
#>>> False

print(check_sudoku(incorrect3))
#>>> False

print(check_sudoku(incorrect4))
#>>> False

print(check_sudoku(incorrect5))
#>>> False


