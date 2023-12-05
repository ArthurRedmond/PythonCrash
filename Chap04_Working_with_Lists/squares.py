squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

squares_list_comprehension = [value**2 for value in range(1,11)]
print(squares_list_comprehension)