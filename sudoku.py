input='295743861\n431865927\n876192543\n387459216\n612387495\n549216738\n763524189\n928671354\n154938672'
sudoku = input.split("\n")
sudoku_numbers = [i for i in range(1,10)]
sudoku_column_list = []
sudoku_subsquare_list = []

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

def check_rows(sudoku_input):
    for row in sudoku_input:
        for number in sudoku_numbers:
            if row.find(str(number)) == -1:
                print(number, "missing: no sudoku. This was found in row ", row)
                break
            else:
                continue
    return True


def check_columns():
    #create a new list made up by the first, second, etc number of each element in list. Use the check_row function to check validity.
    for number in range(len(sudoku_numbers)):
        row_string = ''
        for i in sudoku_numbers:
            row_string += sudoku[i-1][number]
        sudoku_column_list.append(row_string)

    check_rows(sudoku_column_list)

def check_subsquare():


    k = 0

    while k < 9:
        subsquare_string = ''
        for i in range(k,3+k):

            for j in range(k,k+3):
                subsquare_string += sudoku[i][j]
        sudoku_subsquare_list.append(subsquare_string)

        k += 3


    check_rows(sudoku_subsquare_list)
    print(sudoku_subsquare_list)

check_subsquare()