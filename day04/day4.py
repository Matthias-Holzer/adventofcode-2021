import csv

tables = None
tables_hit = []
draws = {}
last_draw = None
part_two = False
bords_that_won = []

output = []

rows = [
        [0,0,0,45,0],
        [1,0,1,45,0],
        [2,0,2,45,0],
        [3,0,3,45,0],
        [4,0,4,45,0]
    ]

def writeToCSV():
    fieldnames = ['draw','board_number', 'idy', 'idx', 'value', 'ticked']
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        print(output)
        for line in output:
            writer.writerow(line)



def one():
    global tables_hit
    global last_draw
    global output
    for idx_draw,draw in enumerate(draws):
        last_draw = draw
        for idx_table,table in enumerate(tables):
            for idx_row,row in enumerate(table):
                for idx_item,item in enumerate(row):
                    if item == draw:
                        tables_hit[idx_table][idx_row][idx_item] = 1
                        output.append([draw, idx_table,idx_row, idx_item, item,  tables_hit[idx_table][idx_row][idx_item]])
                    output.append([draw, idx_table, idx_row, idx_item, item, tables_hit[idx_table][idx_row][idx_item]])
        check_for_bingo()
    writeToCSV()


def two():
    global part_two
    part_two = True
    one()

def check_for_bingo():
    for idx,table in enumerate(tables_hit):
        for row in table:
            if 0 not in row: #checks verticaly
                print('FOUND ONE HORIZONTAL')
                calculate_winning_board(idx)
        for num in range(5): #checks horizontaly
            vertical = [table[0][num],table[1][num],table[2][num],table[3][num],table[4][num]]
            if 0 not in vertical:
                print('FOUND ONE VERTICAL')
                calculate_winning_board(idx)
        left_to_right = [table[0][0],table[1][1],table[2][2],table[3][3],table[4][4]]
        right_to_left = [table[0][4],table[1][3],table[2][2],table[3][1],table[4][0]]
        if 0 not in left_to_right:
            print('FOUND ONE DIAGONAL left_to_right')
            calculate_winning_board(idx)
        if 0 not in right_to_left:
            print('FOUND ONE DIAGONAL right_to_left')
            calculate_winning_board(idx)

def calculate_winning_board(winning_board_number):
    if not winning_board_number in bords_that_won:
        bords_that_won.append(winning_board_number)
    if part_two:
        if len(tables) != len(bords_that_won):
            return
    sum = 0
    umarkt_numbers = []
    for idx_row,row in enumerate(tables[winning_board_number]):
        for idx_item,item in enumerate(row):
            if tables_hit[winning_board_number][idx_row][idx_item] == 0:
                sum += item
                umarkt_numbers.append(item)
    print(f"The Winning Summ is: {sum*last_draw}")
    print(f"The Winning Board is {winning_board_number}")
    print(f"The last Draw was {last_draw}")
    print(f"The sum is {sum} and the index is {winning_board_number}")


def main():
    global draws
    global tables
    file = open('input', 'r')
    read = file.read()
    draws = list(map(int, read.splitlines()[0].split(',')))
    tables = read.split('\n\n')[1:]
    new = []
    for table in tables:
        new.append(table.split('\n'))
    new2 = []
    for y in new:
        for x in y:
            new2.append(list(map(int, x.split())))
    tables = new2
    #tables.remove([])
    new3 = []
    new4 = []
    new5 = []
    for idx, row in enumerate(new2):
        new3.append(row)
        new5.append([0,0,0,0,0])
        if (idx+1) % 5 == 0:
            new4.append(new3)
            new3 = []
            tables_hit.append(new5)
            new5 = []

    tables = new4

    #one()
    two()

if __name__ == "__main__":
    main()