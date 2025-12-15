import matrix
import os


def choose_function(matrix1, matrix2):
    print('''
0) Clear Terminal
1) Print a matrix
2) Add matrices 
3) Multiply Matrices
4) Scalar Multiplication
5) Swap Rows
''')
    choice = str()
    while choice != "0":
        choice = input("Select a feature: ")
        if choice == '0':
            clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
        elif choice == '1':
            matrix_choice = input("Matrix to display (1 or 2): ")
            if matrix_choice == '1':
                matrix1.display()
            elif matrix_choice == '2':
                matrix2.display()
        elif choice == '2':
            matrix.add(matrix1,matrix2)
        elif choice == '3':
            what_by_what = input('''
    1) 1x2
    2) 2x1
    ''')
            if what_by_what == '1':
                matrix.multiply(matrix1,matrix2)
            elif what_by_what == '2':
                matrix.multiply(matrix2, matrix1)
        elif choice == '4':
            m_choice = input('What matrix? (1 or 2)')
            row_choice = int(input("What row:"))
            scale = int(input("Scalar (int): "))
            if m_choice == '1':
                matrix.scalar(matrix1,row_choice, scale)
            elif m_choice == '2':
                matrix.scalar(matrix2,row_choice, scale)
        elif choice == "5":
            m_choice = input('What matrix?:')
            row_choice = input('What rows? (enter row,row e.g. 3,4): ')
            if m_choice == '1':
                matrix.swap_rows(matrix1,row_choice)
            elif m_choice == '2':
                matrix.swap_rows(matrix2,row_choice)            


            


def main():

#Inputs go row count, column count, row1, row2, etc...
    matrix1 = matrix.matrix(4,2,[[1,2],[3,4],[123,423],[54,12]])
    matrix2 = matrix.matrix(2,2,[[5,6],[7,8]])





    

    choose_function(matrix1, matrix2)
    






if __name__ == "__main__":
    main()
