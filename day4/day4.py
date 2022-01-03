import csv

tables = None
tables_hit = []
draws = {}
last_draw = None

def writeToCSV(rows):
    fieldnames = ['table_id', 'idx', 'idy', 'value', 'ticked']

    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fieldnames)
        for row in rows:
            writer.writerow(row)

rows = [
        [0,0,0,45,0],
        [1,0,1,45,0],
        [2,0,2,45,0],
        [3,0,3,45,0],
        [4,0,4,45,0]
    ]

def one():
    global tables_hit
    global last_draw
    for idx_draw,draw in enumerate(draws):
        last_draw = draw
        for idx_table,table in enumerate(tables):
            for idx_row,row in enumerate(table):
                for idx_item,item in enumerate(row):
                    if item == draw:
                        tables_hit[idx_table][idx_row][idx_item] = 1
        check_for_bingo()
        print(tables_hit)
        #exit()

def check_for_bingo():
    for idx,table in enumerate(tables_hit):
        for row in table:
            if 0 not in row: #checks verticaly
                print('FOUND ONE HORIZONTAL')
                print(row)
                calculate_winning_board(idx)
                #exit()
        for num in range(5): #checks horizontaly
            vertical = [table[0][num],table[1][num],table[2][num],table[3][num],table[4][num]]
            if 0 not in vertical:
                print('FOUND ONE VERTICAL')
                print(vertical)
                print(tables[idx])
                calculate_winning_board(idx)
                #exit()
        left_to_right = [table[0][0],table[1][1],table[2][2],table[3][3],table[4][4]]
        right_to_left = [table[0][4],table[1][3],table[2][2],table[3][1],table[4][0]]
        if 0 not in left_to_right:
            print('FOUND ONE DIAGONAL left_to_right')
            calculate_winning_board(idx)
            #exit()
        if 0 not in right_to_left:
            print('FOUND ONE DIAGONAL right_to_left')
            calculate_winning_board(idx)
            #exit()

def calculate_winning_board(winning_board_number):
    sum = 0
    umarkt_numbers = []
    for idx_row,row in enumerate(tables[winning_board_number]):
        for idx_item,item in enumerate(row):
            if tables_hit[winning_board_number][idx_row][idx_item] == 0:
                sum += item
                umarkt_numbers.append(item)
    print(f"The Winning Summ is: {sum*last_draw}")
    print(f"The Winning Board is {winning_board_number}")
    print_table(tables[winning_board_number])
    print(f"The last Draw was {last_draw}")
    print(f"The sum is {sum} and the index is {winning_board_number}")
    print(f"Ther umarkt numbers are {umarkt_numbers}")
    print(draws)
    print(tables)
    print_table(tables)
    exit()

def print_table(table):
    for row in table:
        print("TABLE X")
        print(row)

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
    print(tables)
    print_table(tables)
    print(tables_hit)
    one()

if __name__ == "__main__":
    main()