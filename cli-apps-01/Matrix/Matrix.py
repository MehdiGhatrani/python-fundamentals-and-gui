# import modules and global variable

# get matrix
def get_matrix():
    ROW = 3
    COLUMNS = 3

    print(f"Enter each row with {COLUMNS} values separated by spaces:")
    while True:
        matrix = [list(map(int, input().split())) for _ in range(ROW)]
        if any(len(row)!=3 for row in matrix):
            print("please enter a matrix with 3 columns: ")
            continue

        return matrix

# calculate sum of row
def sum_of_row(matrix:list):
    for row,i in zip(matrix, range(1,4)):
        print(f"row {i}: {sum(row)}")

# calculate sum of columns
def sum_of_columns(matrix):
    for i, h in zip(range(3), range(1,4)):
        c = 0
        for j in range(3):
            c += matrix[j][i]
        print(f"column {h}: {c}")
           

# main
def main():
    matrix = get_matrix()
    sum_of_row(matrix)
    sum_of_columns(matrix)

main()