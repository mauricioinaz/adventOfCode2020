FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def count_adjacents(i, j, seats):
    # previous row
    adjacents = sum([1 for s in seats[i-1][j-1:j+2] if s == OCCUPIED])
    # left
    if seats[i][j-1] == OCCUPIED:
        adjacents += 1
    # right
    if seats[i][j+1] == OCCUPIED:
        adjacents += 1
    # next row
    adjacents += sum([1 for s in seats[i+1][j-1:j+2] if s == OCCUPIED])
    return adjacents


# check if boat seatings are equal
def boats_equal(old, new):
    if len(old) != len(new):
        return False
    for r1, r2 in zip(old, new):
        for s1, s2 in zip(r1, r2):
            if s1 != s2:
                return False
    return True


def print_seats(seats, n):
    print(f'PRINTING A BOAT {n} \n')
    for row in seats:
        print(row)
    print('\n')


# deep copy of boat seatings
def copy_boat(seats):
    new_boat = []
    for row in seats:
        new_row = []
        for seat in row:
            new_row.append(seat)
        new_boat.append(new_row)
    return new_boat


# PART 1
def occupied_seats(seats):
    # Expand floor rows and columns for easier operations
    seats.insert(0, [FLOOR] * len(seats[0]))
    seats.append([FLOOR] * len(seats[0]))
    for row in seats:
        row.insert(0, FLOOR)
        row.append(FLOOR)

    # WAIT UNTIL STABILIZED SEATS
    new_seats = copy_boat(seats)
    old_seats = [[]]
    ctr = 0  # Used to avoid an infinite loop
    while not boats_equal(old_seats, new_seats) and ctr < 300:
        old_seats = copy_boat(new_seats)
        new_seats = copy_boat(seats)
        for i in range(1, len(seats)-1):
            for j in range(1, len(seats[0])-1):
                current_seat = old_seats[i][j]
                if current_seat == EMPTY or current_seat == OCCUPIED:
                    adjacents = count_adjacents(i, j, old_seats)
                    # print(f'{i=} {j=} {current_seat} {adjacents = }')
                    if current_seat == EMPTY and adjacents == 0:
                        new_seats[i][j] = OCCUPIED
                    elif current_seat == OCCUPIED and adjacents >= 4:
                        new_seats[i][j] = EMPTY
                    else:
                        new_seats[i][j] = current_seat
        ctr += 1

        # print_seats(old_seats, 'OLD_SEATS')
        # print_seats(new_seats, 'NEW_SEATS')
        # break

    if ctr >= 300:
        print(f'Exited with INFINITE LOOP')
        return None

    # FINAL COUNT OF OCCUPIED SEATS
    seats_count = 0
    for row in old_seats:
        for seat in row:
            if seat == OCCUPIED:
                seats_count += 1
    return seats_count


# # PART 2
# def encription_weakness(data, number):
#     pass


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [list(row.strip()) for row in puzzle_input]
    print('Part ONE')
    print(f'{occupied_seats(data)}')
    # print('Part TWO')
    # print(f'{encription_weakness(data, wrong_number)}')


if __name__ == "__main__":
    main()
