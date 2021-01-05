SHINY_GOLD = 'shiny gold'


def extract_bag_rules(data):
    rules = {}
    for row in data:
        key, values = row.split('contain')
        key = key[:-6]  # remove ' bags '
        # print(f'--{values}--')
        if values == ' no other bags':
            rules[key] = []
        else:
            values = values.split(',')
            clean_values_rules = [' '.join(value.split()[1:3]) for value in values]
            clean_values_ammounts = [' '.join(value.split()[0]) for value in values]
            rules[key] = (clean_values_rules, clean_values_ammounts)
    return rules


# PART 1
def possible_bags(data):
    all_rules = extract_bag_rules(data)
    carry_gold_count = 0
    for rule in all_rules:
        carry_gold_count += check_rule(rule, all_rules)
    return carry_gold_count


def check_rule(rule, all_rules):
    if not all_rules[rule]:
        return False
    elif SHINY_GOLD in all_rules[rule][0]:
        return True
    else:
        return any([check_rule(rl, all_rules) for rl in all_rules[rule][0]])


# PART 2
def ammount_of_bags(data):
    all_rules = extract_bag_rules(data)
    return count_bags(SHINY_GOLD, all_rules) - 1


def count_bags(rule, all_rules):
    if not all_rules[rule]:
        return 1
    return sum([count_bags(rl, all_rules)*int(mlt) for rl, mlt in zip(*all_rules[rule])]) + 1


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row[:-2] for row in puzzle_input]
    print('Part ONE')
    print(f'{possible_bags(data)}')
    print('Part TWO')
    print(f'{ammount_of_bags(data)}')


if __name__ == "__main__":
    main()
