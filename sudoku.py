no_of_lines = 3
input_lines = ''
for i in range(no_of_lines):
    input_lines += input("Input: ") + "\n"

sudoku_numbers = [i for i in range(1,10)]

sudoku = input_lines.split("\n")[0:no_of_lines]

#What needs to be done?
def check_input():
    #check if entered input has 9 entries and only digits
    for row in sudoku:
        if len(row) != 9:
            print("No valid input", len(row))
            break

        else:
            for number in row:
                if number.isdigit() == False:
                    print("No valid input")
                    break
                else:
                    return True


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
check_rows()