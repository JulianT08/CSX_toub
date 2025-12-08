class matrix:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data
        

def display(self):
    for row in self.data:
        print(row)


def add(matrix1, matrix2):
    if len(matrix1.data) == len(matrix2.data):
        result_matrix = []
        for i in range(len(matrix1.data)):
            row = []
            for j in range(len(matrix1.data[i])):
                row.append(matrix1.data[i][j] + matrix2.data[i][j])
            result_matrix.append(row)
        for row in result_matrix:
            print(row)
    else:
        print("error: dimensions are not the same, cannot add.")


def multiply(first, second):
    if first.cols == second.rows:
        result_matrix = []
        for i in range(len(first.data)):
            row = []
            for j in range(len(second.data[0])):
                product = 0
                for n in range(len(second.data)):
                    product += first.data[i][n] * second.data[n][j] 
                row.append(product)  
            result_matrix.append(row)     
        for row in result_matrix:
            print(row)



def scalar(m,row_choice, scale):
    for row in m.data:
        if row == m.data[row_choice-1]:
            #row = row.split(',')
            result_row = []
            for i in row:
                result_row.append(i*scale)

            print(result_row) 