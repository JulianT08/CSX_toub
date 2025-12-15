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
    else:
        print("Columns of first matrix does not equal the rows of the second matrix")



def scalar(m,row_choice, scale):
    for row in m.data:
        if row == m.data[row_choice-1]:
            #row = row.split(',')
            result_row = []
            for i in row:
                result_row.append(i*scale)

            print(result_row) 


def swap_rows(m, row_choice):
    rows = row_choice.split(',')
    row1 = int(rows[0]) - 1
    row2 = int(rows[1]) - 1
    row1_data = m.data[row1]
    row2_data = m.data[row2]
    index1 = m.data.index(row1_data)
    index2 = m.data.index(row2_data)
    result_matrix = []
    for row in m.data:
        if row != row1_data and row != row2_data:
            result_matrix.append(row)
    result_matrix.insert(index1,row2_data)
    result_matrix.insert(index2,row1_data)
    for row in result_matrix:
        print(row)