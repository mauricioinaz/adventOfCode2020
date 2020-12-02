# PART 1
def get_two_entries(input):
    for i, first_numb in enumerate(input):
        for second_numb in input[i:]:
            if first_numb + second_numb == 2020:
                return f'{first_numb} * {second_numb} = {first_numb*second_numb}'
    return None


# PART 2  (First solution)
def get_three_entries(input):
    pairs = []
    for i, first_numb in enumerate(input):
        for second_numb in input[i:]:
            if first_numb + second_numb <= 2020:
                pairs.append([first_numb, second_numb])
    for third_numb in input:
        for pair in pairs:
            if pair[0] + pair[1] + third_numb == 2020:
                return f'{pair[0]} * {pair[1]} * {third_numb} = {pair[0]*pair[1]*third_numb}'
    return None

# # PART 2  (Second Solution)
# def get_three_entries(input):
#     for i, first_numb in enumerate(input):
#         for j, second_numb in enumerate(input[i:]):
#             for third_numb in input[i+j:]:
#                 if first_numb + second_numb + third_numb == 2020:
#                     return f'{first_numb} * {second_numb} * {third_numb} = {first_numb*second_numb*third_numb}'
#     return None


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [int(row.strip()) for row in puzzle_input]
    print('Part ONE')
    print(get_two_entries(data))
    print('Part TWO')
    print(get_three_entries(data))


if __name__ == "__main__":
    main()
