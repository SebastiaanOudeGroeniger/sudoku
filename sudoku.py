input='295743861\n431865927\n176192543\n387459216\n612387495\n549216738\n763524189\n928671354\n154938672'
sudoku = input.split("\n")
sudoku_numbers = [i for i in range(1,10)]



def check_input():
    #check if entered input has 9 entries and only digits
    for row in sudoku:
        if len(row) == 9:
            for number in row:
                if number.isdigit() == False:
                    print("No valid input, not all numbers:", number)
                    break
                else:
                    continue
        elif len(row) != 9:
            for number in row:
                if number.isdigit() == False:
                    print("No valid input, not all numbers:", number)
                    break
                else:
                    continue
            print("No valid input, more than 9 numbers:", len(row))
        else:
            return True




check_input()

'''
def check_rows():
    for row in sudoku:
        for number in sudoku_numbers:
            if row.find(str(number)) == -1:
                print(number, "missing: no sudoku. This was found in row ", row)
                break
            else:
                return True

def check_columns():

    for row in range(3):

        for column in range(3):
            sudoku_column = []
            sudoku_column.append((sudoku[row][column]))
    print(sudoku_column)



        #print(sudoku[column][column])

    pass
    # check if column has 1 to 9


def check_subsquare():
    pass
    # check if subsquare has 1 to 9

check_columns()

check_input()
check_rows()'''