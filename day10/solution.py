

# PART 1
def jolt_differences(data):
    # add outlet
    data.append(0)
    # add built-in adapter
    data.append(max(data)+3)
    data.sort()
    ones = 0
    threes = 0
    for i, adpt_1 in enumerate(data, start=1):
        if i == len(data):
            break
        adpt_2 = data[i]
        diff = adpt_2 - adpt_1
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
        else:
            raise Exception(f'unexpected difference: {diff}')
    print(f'{ones = } AND {threes = }')
    return ones * threes

# # PART 2
# def encription_weakness(data, number):
#     pass


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [int(row.strip()) for row in puzzle_input]
    print('Part ONE')
    print(f'{jolt_differences(data)}')
    # print('Part TWO')
    # print(f'{encription_weakness(data, wrong_number)}')


if __name__ == "__main__":
    main()
