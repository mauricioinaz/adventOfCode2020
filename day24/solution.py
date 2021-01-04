NORTH_SOUTH = ['n', 's']
BLACK = True
WHITE = False
E = 'e'
SE = 'se'
SW = 'sw'
W = 'w'
NW = 'nw'
NE = 'ne'
HEX_COMPASS = {
    #   ( Y,  X)
    E:   (0,  1),
    SE:  (1,  1),
    SW:  (1,  0),
    W:   (0, -1),
    NW: (-1, -1),
    NE: (-1,  0)
}


def get_flip_list(data):
    tiles_list = []
    for line in data:
        line = line.strip()
        tile_position = []
        while line:
            if line[0] in NORTH_SOUTH:
                tile_position.append(line[:2])
                line = line[2:]
            else:
                tile_position.append(line[:1])
                line = line[1:]
        tiles_list.append(tile_position)

    return tiles_list


# PART 1
def lobby_layout(data):
    flip_list = get_flip_list(data)
    max_instructions = max([len(it) for it in flip_list])*2 + 1
    grid = [[WHITE for i in range(max_instructions)] for _ in range(max_instructions)]
    for flip_instructions in flip_list:
        x = y = max_instructions // 2
        location = (y, x)  # REFERENCE TILE
        for instr in flip_instructions:
            location = tuple(prev + step for prev, step in zip(location, HEX_COMPASS[instr]))
        grid[location[0]][location[1]] = not grid[location[0]][location[1]]  # flip color

    return sum([sum(y) for y in grid])


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{lobby_layout(data)}')


if __name__ == "__main__":
    main()
