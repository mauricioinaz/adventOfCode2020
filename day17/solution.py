INACTIVE = '.'
ACTIVE = '#'


# PART 1
def six_cycles_3d(data):
    p_input = [list(row.strip()) for row in data]
    input_size = len(p_input)
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
# Same as part 1, but 4d, not DRY at all :(
def six_cycles_4d(data):
    p_input = [list(row.strip()) for row in data]
    input_size = len(p_input)
    grid_size = input_size + 6*2
    center = grid_size//2
    grid = [[[[INACTIVE for d1 in range(grid_size)] for d2 in range(grid_size)] for d3 in range(grid_size)] for d4 in range(grid_size)]

    # put input in center of grid
    for x_ind, x in enumerate(grid[center][center]):
        if 6 <= x_ind < input_size+6:
            grid[center][center][x_ind][6:(input_size+6)] = p_input[x_ind-6]

    cycle = 0
    while cycle < 6:
        # print_grid_4d(grid, cycle)
        new_grid = [[[[INACTIVE for d1 in range(grid_size)] for d2 in range(grid_size)] for d3 in range(grid_size)] for d4 in range(grid_size)]
        for z_ind, z in enumerate(grid):
            for w_ind, w in enumerate(z):
                for x_ind, x in enumerate(w):
                    for y_ind, y in enumerate(x):
                        neighbors = count_neighbors_4d(z_ind, w_ind, x_ind, y_ind, grid)
                        if y == ACTIVE and (2 <= neighbors <= 3):
                            new_grid[z_ind][w_ind][x_ind][y_ind] = ACTIVE
                        elif y == INACTIVE and neighbors == 3:
                            new_grid[z_ind][w_ind][x_ind][y_ind] = ACTIVE
        cycle += 1
        grid = new_grid
    count = 0
    for z in grid:
        for w in z:
            for x in w:
                for y in x:
                    if y == ACTIVE:
                        count += 1
    return count


def count_neighbors_4d(z, w, x, y, grid):
    count = 0
    for z_ind, z_dim in enumerate(grid[z-1:z+2]):
        for w_ind, w_dim in enumerate(z_dim[w-1:w+2]):
            for x_ind, x_dim in enumerate(w_dim[x-1:x+2]):
                for y_ind, y_dim in enumerate(x_dim[y-1:y+2]):
                    if z_ind == 1 and w_ind == 1 and x_ind == 1 and y_ind == 1:
                        # skip center
                        continue
                    elif y_dim == ACTIVE:
                        count += 1
    return count


def print_grid_4d(grid, n):
    print(f'PRINTING grid cycle {n} \n')
    for ind, z in enumerate(grid[5:9], 5):
        print('¡¡NEW Z!!')
        print(ind)
        for ind_w, w in enumerate(z):
            print(ind_w)
            for x in w:
                print(x)
            print('\n')


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{six_cycles_3d(data)}')
    print('Part TWO')
    print(f'{six_cycles_4d(data)}')


if __name__ == "__main__":
    main()
