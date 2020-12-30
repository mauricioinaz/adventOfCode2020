def get_tiles(data):
    tiles = {}
    tmp = []
    for line in data:
        line = line.strip()
        if line[:4] == 'Tile':
            key = int(line[5:9])
            tmp = []
        elif line:
            tmp.append(line)
        else:
            tiles[key] = tmp
    tiles[key] = tmp
    return tiles


# PART 1
def get_adjacents_mult(data):
    tiles = get_tiles(data)
    borders = {k: set() for k in tiles.keys()}
    for k1, tl1 in tiles.items():
        sides1 = get_sides(tl1)
        # compare sides with rest of tiles
        rest_of_tiles = {ky: tile for ky, tile in tiles.items() if ky != k1}
        for k2, tl2 in rest_of_tiles.items():
            sides2 = get_sides(tl2)
            for side in sides1:
                # add border by comparing normal or flipped
                if side in sides2 or side[::-1] in sides2:
                    borders[k1].add(k2)
    # multiply ID which only have 2 borders ie CORNERS
    result = 1
    for k, brd in borders.items():
        if len(brd) == 2:
            result *= k
    return result


def get_sides(tl):
    # add first and last
    sides = [tl[0], tl[-1]]
    # add left and right sides
    left = []
    right = []
    for line in tl:
        left.append(line[0])
        right.append(line[-1])
    sides.append(''.join(left))
    sides.append(''.join(right))
    return sides


# # PART 2
# def get_results(data):
#     pass


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_adjacents_mult(data)}')
    # print('Part TWO')
    # print(f'{get_results(data)}')


if __name__ == "__main__":
    main()
