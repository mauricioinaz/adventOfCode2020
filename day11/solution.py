FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'


def count_adjacents(i, j, seats, can_see=False):
    if can_see:
        return count_seable_adjacents(i, j, seats)
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


def check_limit(numb, limit):
    if limit == 0:
        return numb > limit
    return numb < limit


def seable_seat(seats, y, x, lim_y, lim_x, up, right):
    viewing = FLOOR
    while check_limit(x, lim_x) and check_limit(y, lim_y) and viewing == FLOOR:
        viewing = seats[y][x]
        if viewing == OCCUPIED:
            return 1
        elif viewing == EMPTY:
            return 0
        y += up
        x += right

    return 0


def count_seable_adjacents(i, j, seats):
    adjacents = 0

    # up
    adjacents += seable_seat(seats, i-1, j, 0, 0, -1, 0)
    # down
    adjacents += seable_seat(seats, i+1, j, len(seats), 0, 1, 0)

    # left
    adjacents += seable_seat(seats, i, j-1, 0, 0, 0, -1)
    # right
    adjacents += seable_seat(seats, i, j+1, 0, len(seats[0]), 0, +1)

    # up-left
    adjacents += seable_seat(seats, i-1, j-1, 0, 0, -1, -1)
    # up-right
    adjacents += seable_seat(seats, i-1, j+1, 0, len(seats[0]), -1, 1)

    # down-left
    adjacents += seable_seat(seats, i+1, j-1, len(seats), 0, 1, -1)
    # down-right
    adjacents += seable_seat(seats, i+1, j+1, len(seats), len(seats[0]), 1, 1)

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


# PART 1 and 2
def occupied_seats(seats, can_see=False):
    # Expand floor rows and columns for easier operations
    seats.insert(0, [FLOOR] * len(seats[0]))
    seats.append([FLOOR] * len(seats[0]))
    for row in seats:
        row.insert(0, FLOOR)
        row.append(FLOOR)

    # WAIT UNTIL STABILIZED SEATS
    new_seats = copy_boat(seats)
    old_seats = [[]]
    occupied_limit = 5 if can_see else 4
    ctr = 0  # Used to avoid an infinite loop
    loop_limit = 300
    while not boats_equal(old_seats, new_seats) and ctr < loop_limit:
        old_seats = copy_boat(new_seats)
        new_seats = copy_boat(seats)
        for i in range(1, len(seats)-1):
            for j in range(1, len(seats[0])-1):
                current_seat = old_seats[i][j]
                if current_seat == EMPTY or current_seat == OCCUPIED:
                    adjacents = count_adjacents(i, j, old_seats, can_see)
                    if current_seat == EMPTY and adjacents == 0:
                        new_seats[i][j] = OCCUPIED
                    elif current_seat == OCCUPIED and adjacents >= occupied_limit:
                        new_seats[i][j] = EMPTY
                    else:
                        new_seats[i][j] = current_seat

        ctr += 1

    if ctr >= loop_limit:
        print(f'Exited with {loop_limit =}')
        return None

    # FINAL COUNT OF OCCUPIED SEATS
    seats_count = 0
    for row in old_seats:
        for seat in row:
            if seat == OCCUPIED:
                seats_count += 1
    return seats_count


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [list(row.strip()) for row in puzzle_input]
    print('Part ONE')
    print(f'{occupied_seats(data)}')
    print('Part TWO')
    print(f'{occupied_seats(data, True)}')


if __name__ == "__main__":
    main()
