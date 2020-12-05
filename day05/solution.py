# PART 1
def find_seats(data):
    biggest_seatID = 0
    airplane = [[False for y in range(0, 8)] for x in range(0, 128)]
    for ticket in data:
        row = int(ticket[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(ticket[-3:].replace('R', '1').replace('L', '0'), 2)
        seat_ID = row*8 + column
        airplane[row][column] = True
        if seat_ID > biggest_seatID:
            biggest_seatID = seat_ID
    return airplane, biggest_seatID


# PART 2
def find_my_seat(airplane):
    cleared_front = False
    for r, row in enumerate(airplane):
        if cleared_front and not all(row):
            return r*8 + row.index(False)
        elif any(row):
            cleared_front = True

    return 'No seat found :('


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    airplane, biggest_ID = find_seats(data)
    my_ID = find_my_seat(airplane)
    print('Part ONE')
    print(f'{biggest_ID = }')
    print('Part TWO')
    print(f'{my_ID = }')


if __name__ == "__main__":
    main()
