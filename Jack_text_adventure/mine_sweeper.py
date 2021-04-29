rows = 4
cols = 4

# The manually created board list
# This is a 2D list, so each element is actually another list!
board = [
    ['1', '1', '1', '0'],
    ['1', 'X', '2', '1'],
    ['1', '1', '2', 'X'],
    ['0', '0', '1', '1']
]

# This is another 2D list to determine if each square should be showing
revealed = [
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False],
    [False, False, False, False]
]

# This is a function, very powerful, but confusing,
# don't worry about understanding all of how it works
def reveal_board(row, col):
    # If the square isn't already revealed
    if not revealed[row][col]:
        # Then we reveal it
        revealed[row][col] = True
        if board[row][col] != '0':
            # If the square isn't empty, then we don't continue revealing
            return
        # This loops through the squares all around the chosen square
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                # If the new row or new col would be invalid, skip this loop
                if row + i < 0 or row + i > rows - 1:
                    continue
                if col + j < 0 or col + j > cols - 1:
                    continue
                # If everything checks out, then we can call this function again
                # on the surrounding square we're at in the double for loop
                reveal_board(row + i, col + j)


# Loop forever (or until we break)
while True:
    # print the map:
    # Loop over the number of rows, will be from 0 to 3 (remember 0 indexed lists!)
    for row in range(rows):
        # A nested for loop, this will run each time the outer one runs
        for col in range(cols):
            # We can index into a 2D list with two sets of brackets []
            if revealed[row][col]:
                # If the square should be shown, show the actual character at that square
                # The end='' just makes the print not print a new line at the end
                print(board[row][col] + " ", end='')
            else:
                # Otherwise, should print a default #
                print('# ', end='')
        # Print new lines for formatting
        print()
    print()
    # We've seen input before, but we're casting the value we get to an integer
    row_choice = int(input("pick a row (starting from the top left, 0 indexed): "))
    col_choice = int(input("pick a col (starting from the top left, 0 indexed): "))

    # Now we check if they chose a mine
    choice_char = board[row_choice][col_choice]
    if choice_char == 'X':
        # The game is over so we have to break out of the infininte loop
        print("You Lost!")
        break
    else:
        # We make a function call to reveal the choice and other nearby squares
        reveal_board(row_choice, col_choice)

    # This is the implicit end of the while loop
        

#print the board once more after you lose:
for row in range(rows):
    for col in range(cols):
        if revealed[row][col]:
            print(board[row][col] + " ", end='')
        else:
            print('# ', end='')
    print()
print()

            

