
class sudoku:

    numChanges = 0
    empty = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sandbox = [[8, 0, 0, 0, 0, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 0, 9, 0, 0],
                [0, 4, 5, 1, 0, 0, 0, 2, 0],
                [0, 9, 0, 0, 0, 4, 0, 0, 0],
                [0, 2, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 2],
                [0, 0, 0, 7, 0, 0, 1, 0, 0],
                [0, 3, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 9, 0, 0, 6]]

    solved = [[4, 3, 5, 2, 6, 9, 7, 8, 1],
              [6, 8, 2, 5, 7, 1, 4, 9, 3],
              [1, 9, 7, 8, 3, 4, 5, 6, 2],
              [8, 2, 6, 1, 9, 5, 3, 4, 7],
              [3, 7, 4, 6, 8, 2, 9, 1, 5],
              [9, 5, 1, 7, 4, 3, 6, 2, 8],
              [5, 1, 9, 3, 2, 6, 8, 7, 4],
              [2, 4, 8, 9, 5, 7, 1, 3, 6],
              [7, 6, 3, 4, 1, 8, 2, 5, 9]]

    solvable = [[4, 0, 5, 2, 6, 9, 7, 8, 1],
                [6, 8, 2, 5, 7, 1, 4, 0, 3],
                [1, 9, 7, 8, 3, 4, 5, 6, 2],
                [8, 2, 6, 1, 9, 5, 3, 4, 7],
                [3, 7, 0, 6, 8, 2, 9, 1, 5],
                [9, 5, 1, 7, 4, 3, 6, 2, 8],
                [5, 1, 9, 3, 0, 6, 0, 7, 4],
                [2, 4, 0, 9, 5, 7, 1, 3, 6],
                [7, 6, 3, 4, 1, 0, 2, 5, 9]]

    hard = [[2, 0, 0, 5, 0, 7, 4, 0, 6],
            [0, 0, 0, 0, 3, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 2, 3, 0],
            [0, 0, 0, 0, 2, 0, 0, 0, 0],
            [8, 6, 0, 3, 1, 0, 0, 0, 0],
            [0, 4, 5, 0, 0, 0, 0, 0, 0],
            [0, 0, 9, 0, 0, 0, 7, 0, 0],
            [0, 0, 6, 9, 5, 0, 0, 0, 2],
            [0, 0, 1, 0, 0, 6, 0, 0, 8]]

    easy = [[0, 0, 6, 0, 0, 0, 8, 4, 3],
            [0, 8, 0, 0, 5, 0, 6, 2, 0],
            [0, 0, 0, 0, 0, 3, 5, 0, 0],
            [0, 0, 0, 6, 2, 7, 0, 0, 8],
            [0, 0, 8, 0, 9, 0, 0, 3, 0],
            [0, 9, 0, 0, 0, 0, 0, 5, 4],
            [0, 0, 2, 0, 8, 6, 3, 9, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 3, 5, 0, 0, 0]]

    hardest = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 3, 6, 0, 0, 0, 0, 0],
               [0, 7, 0, 0, 9, 0, 2, 0, 0],
               [0, 5, 0, 0, 0, 7, 0, 0, 0],
               [0, 0, 0, 0, 4, 5, 7, 0, 0],
               [0, 0, 0, 1, 0, 0, 0, 3, 0],
               [0, 0, 1, 0, 0, 0, 0, 6, 8],
               [0, 0, 8, 5, 0, 0, 0, 1, 0],
               [0, 9, 0, 0, 0, 0, 4, 0, 0]]

    table = hardest

    def __init__(self):
        print("Table start: ")

        self.__printTable()
        if self.__isValidTable():
            if self.__driver():
                print("Solved Table")
                self.__printTable()
        else:
            print("not solvable")


    def __printTable(self, ro = -1, co = -1, message = ""):

        if message != "":
            print(message)

        for r in range(0,9):
            #Prints horizontal borders
            if r == 0 or r == 3 or r == 6:
                self.__printLine('=')

            for c in range(0,9):

                #Prints bold vertical borders
                if c == 0 or c == 3 or c == 6:
                    print('|', end = '')

                #Prints normal border
                print('|', end = " ")

                #Stars to keep track of thing
                if r == ro and c == co:
                    print('*', end = '')

                    if self.table[r][c] == 0:
                        print('#', end='* ')
                    else:
                        print(self.table[r][c], end = '* ')

                elif self.table[r][c] == 0:
                    print('', '#', end = '  ')
                else:
                    print(' ', end = '')
                    print(self.table[r][c], end = '  ')

            #New Line
            print("||")

        #Last Horizontal line
        self.__printLine('=')
        print("Number of changes: ", self.numChanges, '\n')


    def __printLine(self, char):
        for i in range(0,59):
            print(char, end = '')
        print()


    def __isValidTable(self):
        for r in range(0,9):
            for c in range(0,9):
                if self.table[r][c] != 0:
                    if not self.__validPrintedNumber(self.table[r][c], r, c):
                        return False

        return True

    def __driver(self, r=0, c=0):
        end = 9

        if r == end or c == end:
            return True

        elif self.table[r][c] == 0:
            if self.solve(r, c):
                return True

        else:
            tr, tc = self.incrementer(r, c)
            return self.__driver(tr, tc)


    #INCREMENTER
    def incrementer(self, r, c):
        end = 8

        if c == end:
            return r + 1, 0

        return r, c + 1



    def solve(self, r, c):

        solved = False

        for num in range(1,10):
            if self.__validNumber(num, r, c):
                self.table[r][c] = num
                self.numChanges += 1

                tr, tc = self.incrementer(r, c)
                solved = self.__driver(tr, tc)
                if solved: break

                self.table[r][c] = 0
                self.numChanges += 1

        return solved

    def __validNumber(self, num, r, c):
        return not self.inColumn(num, c) and not self.inRow(num, r) and not self.inBox(num, r, c)

    def __validPrintedNumber(self, num, r, c):
        tr = self.__coordinateAssigner(r)
        tc = self.__coordinateAssigner(c)
        return self.__onlyNumInColumn(c) and self.__onlyNumInRow(r) and self.__onlyNumInBox(tr, tc)

    def inColumn(self, num, c, r=0):
        if r == 9:
            #print(1)
            return False
        if self.table[r][c] == num:
            return True
        return self.inColumn(num, c, r + 1)


    def inRow(self, num, r, c=0):
        if c == 9:
            #print(2)
            return False
        if self.table[r][c] == num:
            return True
        return self.inRow(num, r, c + 1)

    #box picker
    def inBox(self, num, r, c):
        tempRow = self.__coordinateAssigner(r)
        tempCol = self.__coordinateAssigner(c)
        return self.__checkBox(num, tempRow, tempCol)

    #for new numbers
    def __checkBox(self, num, r, c):

        return self.table[r][c] == num or \
               self.table[r + 1][c + 1] == num or \
               self.table[r - 1][c - 1] == num or \
               self.table[r + 1][c] == num or \
               self.table[r - 1][c] == num or \
               self.table[r][c + 1]  == num or \
               self.table[r][c - 1] == num or \
               self.table[r + 1][c - 1] == num or \
               self.table[r - 1][c + 1] == num

    #checks box for dupes
    def __onlyNumInBox(self, r, c):
        nums = []
        nums.append(self.table[r][c])
        nums.append(self.table[r + 1][c + 1])
        nums.append(self.table[r - 1][c - 1])
        nums.append(self.table[r + 1][c])
        nums.append(self.table[r - 1][c])
        nums.append(self.table[r][c + 1])
        nums.append(self.table[r][c - 1])
        nums.append(self.table[r + 1][c - 1])
        nums.append(self.table[r - 1][c + 1])

        return self.hasDuplicates(nums)

    #checks row for dupes
    def __onlyNumInRow(self, r):
        nums = []
        for i in range(0, 9):
            nums.append(self.table[r][i])

        return self.hasDuplicates(nums)

    #checks col for dupes
    def __onlyNumInColumn(self, c):
        nums = []
        for i in range (0, 9):
            nums.append(self.table[i][c])

        return self.hasDuplicates(nums)

    def hasDuplicates(self, array):
        try:
            while True:
                array.remove(0)
        except ValueError:
            pass

        #print(array)
        return len(array) == len(set(array))


    def __coordinateAssigner(self, num):
        if 0 <= num and num < 3:
            return 1
        if 3 <= num and num < 6:
            return 4
        if 6 <= num and num < 9:
            return 7

if __name__ == '__main__':
    sudoku()

'''
CODE ARCHIVES

INCREMENTER
        end = 8
        if r == end and c == end:
            print("Solved :D")
            return True

        if c == end:
            self.__driver(r + 1, 0, end)
            return True

        self.__driver(r, c + 1, end)

        return True
'''