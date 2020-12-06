# PART 1
def find_groups(data):
    group = ''
    group_sum = 0
    for row in data:
        if row:
            group += row
        else:
            group_sum += len(set(group))
            group = ''
    group_sum += len(set(group))
    return group_sum


# PART 2
def find_groups_2(data):
    group = set(data[0])
    group_sum = 0
    for i, row in enumerate(data):
        if row:
            group = group.intersection(set(row))
        else:
            group_sum += len(set(group))
            group = set(data[i+1])
    group_sum += len(set(group))
    return group_sum


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    print('Part ONE')
    print(f'{find_groups(data)}')
    print('Part TWO')
    print(f'{find_groups_2(data)}')


if __name__ == "__main__":
    main()
