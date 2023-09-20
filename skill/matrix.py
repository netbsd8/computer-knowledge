# sub-matrix: 9x9 -> 3x3 (Valid Sudoku)
for i in range(9):
    for j in range(9):
        k = i // 3
        l = j // 3
        sub_index = k * 3 + l
