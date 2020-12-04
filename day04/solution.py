import string


def extract_passports(data):
    passports = []
    tmp_passport = {}
    for row in data:
        if row:
            row_values = row.split()
            for pair in row_values:
                key, value = pair.split(":")
                tmp_passport[key] = value
        else:
            passports.append(tmp_passport)
            tmp_passport = {}
    if tmp_passport:
        passports.append(tmp_passport)
    return passports


# PART 1
def valid_passports(data, check_fields=False):
    passports = extract_passports(data)
    valid_passport_count = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
    for passport in passports:
        diff = required_fields.difference(set(passport.keys()))
        if not diff or diff == {'cid'}:
            if not check_fields:
                valid_passport_count += 1
            elif check_passport_fields(passport):
                valid_passport_count += 1

    return valid_passport_count


# PART 2
def check_passport_fields(passport):
    # check Birth Year
    byr = int(passport['byr'])
    if not(1920 <= byr <= 2002):
        # print(f'ERROR {byr = }')
        return False

    # check Issue Year
    iyr = int(passport['iyr'])
    if not(2010 <= iyr <= 2020):
        # print(f'ERROR {iyr = }')
        return False

    # check Expiration Year
    eyr = int(passport['eyr'])
    if not(2020 <= eyr <= 2030):
        # print(f'ERROR {eyr = }')
        return False

    # check Height
    hgt = passport['hgt'][:-2]
    hgt_type = passport['hgt'][-2:]
    if not(hgt_type == 'cm' or hgt_type == 'in'):
        # print(f'ERROR {hgt = } --1')
        return False
    if not hgt.isnumeric():
        # print(f'ERROR {hgt = } --2')
        return False
    hgt = int(hgt)
    if hgt_type == 'cm' and not(150 <= hgt <= 193):
        # print(f'ERROR {hgt = } --3')
        return False
    if hgt_type == 'in' and not(59 <= hgt <= 76):
        # print(f'ERROR {hgt = } --4')
        return False

    # check Hair Color
    hcl_hash = passport['hcl'][0]
    hcl_value = passport['hcl'][1:]
    if not(hcl_hash == '#' and len(hcl_value) == 6 and all(c in string.hexdigits for c in hcl_value)):
        # print(f'ERROR {hcl_hash = } {hcl_value = }')
        return False

    # check Hair Color
    eye_color_values = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    ecl = passport['ecl']
    if ecl not in eye_color_values:
        # print(f'ERROR {ecl = }')
        return False

    # check Passport ID
    pid = passport['pid']
    if not(len(pid) == 9 and pid.isnumeric()):
        # print(f'ERROR {pid = }')
        return False

    return True


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    print('Part ONE')
    print(valid_passports(data))
    print('Part TWO')
    print(valid_passports(data, True))


if __name__ == "__main__":
    main()
