
def star(row, cols):

    for i in range(1, row+1):
        for j in range(1, i):
            print(end=" ")

        for j in range(1, cols+1):
            if(i == 1 or i == row or j == 1 or j == cols):
                print("*", end="")
            else:
                print(end=" ")
        print()


row, cols = 4, 8
star(row, cols)
