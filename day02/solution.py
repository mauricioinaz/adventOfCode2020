def extract_data(row):
    rule, pswd = row.split(":")
    pswd = pswd.strip()
    range, letter = rule.split()
    min, max = range.split("-")
    min = int(min)
    max = int(max)
    return min, max, letter, pswd


# PART 1
def get_valid_password_count(input):
    valid_password_count = 0
    for row in input:
        # cleanup
        min, max, letter, pswd = extract_data(row)
        # validation
        count = len([lt for lt in pswd if lt == letter])
        if min <= count <= max:
            valid_password_count += 1

    return valid_password_count


# PART 2
def get_valid_password_count_pt2(input):
    valid_password_count = 0
    for row in input:
        # cleanup
        pos_1, pos_2, letter, pswd = extract_data(row)
        pos_1 -= 1
        pos_2 -= 1
        # validation
        valid_1 = pswd[pos_1] == letter
        valid_2 = pswd[pos_2] == letter
        if (valid_1 and not(valid_2)) or (valid_2 and not(valid_1)):
            valid_password_count += 1

    return valid_password_count


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    print('Part ONE')
    print(get_valid_password_count(data))
    print('Part TWO')
    print(get_valid_password_count_pt2(data))


if __name__ == "__main__":
    main()
