
def print_matrix_in_circular(A):
    col_min = 0
    col_max = len(A[0])
    row_min = 0
    row_max = len(A)
    row = col = 0

    while col_min < col_max and row_min < row_max:

        for col in range(col_min, col_max):
            print(A[row][col], end=' ')
        else:
            row_min += 1
            #print(f'col={col} row_min={row_min}')

        for row in range(row_min, row_max):
            print(A[row][col], end=' ')
        else:
            col_max -= 1
        # print(f'col_max={col_max}')
        for col in range(col_max-1, col_min-1, -1):
            print(A[row][col], end=' ')
        else:
            row_max -= 1

        for row in range(row_max-1, row_min-1, -1):
            print(A[row][col], end=' ')
        else:
            col_min += 1


if __name__ == '__main__':
    A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print_matrix_in_circular(A)
    print()
    B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
    print_matrix_in_circular(B)

