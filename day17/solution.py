INACTIVE = '.'
ACTIVE = '#'

# PART 1
def six_cycles(data):
    p_input = [list(row.strip()) for row in data]
    input_size = len(p_input)
    # size_z = input_size*2 + 1
    # size_xy = input_size*3
    grid_size = input_size + 6*2
    center = grid_size//2
    grid = [[[INACTIVE for d1 in range(grid_size)] for d2 in range(grid_size)] for d3 in range(grid_size)]

    # put input in center of grid
    for x_ind, x in enumerate(grid[center]):
        if 6 <= x_ind < input_size+6:
            grid[center][x_ind][6:(input_size+6)] = p_input[x_ind-6]

    cycle = 0
    while cycle < 6:
        # print_grid(grid, cycle)
        new_grid = [[[INACTIVE for d1 in range(grid_size)] for d2 in range(grid_size)] for d3 in range(grid_size)]
        for z_ind, z in enumerate(grid):
            for x_ind, x in enumerate(z):
                for y_ind, y in enumerate(x):
                    neighbors = count_neighbors(z_ind, x_ind, y_ind, grid)
                    # print(neighbors)
                    if y == ACTIVE and (2 <= neighbors <= 3):
                        new_grid[z_ind][x_ind][y_ind] = ACTIVE
                    elif y == INACTIVE and neighbors == 3:
                        new_grid[z_ind][x_ind][y_ind] = ACTIVE
        cycle += 1
        grid = new_grid
    count = 0
    for z in grid:
        for x in z:
            for y in x:
                if y == ACTIVE:
                    count += 1
    return count


def count_neighbors(z, x, y, grid):
    count = 0
    for z_ind, z_dim in enumerate(grid[z-1:z+2]):
        for x_ind, x_dim in enumerate(z_dim[x-1:x+2]):
            for y_ind, y_dim in enumerate(x_dim[y-1:y+2]):
                if z_ind == 1 and x_ind == 1 and y_ind == 1:
                    # skip center
                    continue
                elif y_dim == ACTIVE:
                    count += 1
    return count


def print_grid(grid, n):
    print(f'PRINTING grid cycle {n} \n')
    for ind, z in enumerate(grid):
        print(ind)
        for x in z:
            print(x)
            print('\n')


# PART 2
def get_rules_order(valid_tickets, rules):
    pass


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    six_cycles(data)
    print(f'{six_cycles(data)}')
    # print('Part TWO')
    # rules_order = get_rules_order(valid_tickets, rules)
    # print(f'{get_departures(rules_order, my_ticket)}')


if __name__ == "__main__":
    main()
