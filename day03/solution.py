TREE = '#'


# PART 1
def trees_encountered(data, x_inc, y_inc):
    x = 0
    tree_count = 0
    pattern_size = len(data[0]) - 1
    for y in range(y_inc, len(data), y_inc):
        x += x_inc
        tree_row = data[y]
        position = tree_row[x % pattern_size]
        if position == TREE:
            tree_count += 1

    return tree_count


# PART 2
def check_slopes(data):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    result = 1
    for slope in slopes:
        result *= trees_encountered(data, *slope)
    return result


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row for row in puzzle_input]
    print('Part ONE')
    print(trees_encountered(data, 3, 1))
    print('Part TWO')
    print(check_slopes(data))


if __name__ == "__main__":
    main()
