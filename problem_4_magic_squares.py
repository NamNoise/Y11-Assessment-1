from testhelper import test

def is_square_magic(square):
    magic_sum = sum(square[0])
    for row in square:
        if sum(row) != magic_sum:
            return False
    
    for col in range(len(square)):
        if sum(square[row][col] for row in range(len(square))) != magic_sum:
            return False
    






### TESTS - Run the code that calls the function to check it works.
valid_square = [[4, 9, 2], 
          [3, 5, 7], 
          [8, 1, 6]]

invalid_square = [[4, 9, 2], 
          [8, 1, 6],
          [3, 5, 7]]

test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))