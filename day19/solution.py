def get_data(data):
    # Get rules
    rules = {}
    for i, r in enumerate(data):
        row = r.strip()
        # finished reading rules
        if not row:
            break

        key, values = row.split(':')
        key = int(key)
        values = values.strip().split(' ')

        # single letter rule as STRING
        if values == ['"a"'] or values == ['"b"']:
            values = values[0][1]
        # two lists rules as TUPLE of LISTS
        elif '|' in values:
            ind = values.index('|')
            values = (list(map(int, values[:ind])), list(map(int, values[ind+1:])))
        # list of rules as LIST
        else:
            values = list(map(int, values))

        rules[key] = values

    # Get messages
    messages = []
    for ln in data[i+1:]:
        values = ln.strip()
        messages.append(values)

    return rules, messages


# PART 1
def get_results(data):
    rules, messages = get_data(data)
    possibilities = get_possibilites(rules, rules[0])
    valid_options = get_all_possible(possibilities)
    checked = [msg for msg in messages if msg in valid_options]
    print(checked)
    return len(checked)


def get_possibilites(rules, current_rule, rec=[]):
    if type(current_rule) == str:
        return current_rule
    elif type(current_rule) == list:
        return [get_possibilites(rules, rules[rl]) for rl in current_rule]
    elif type(current_rule) == tuple:
        return ([get_possibilites(rules, rules[rl]) for rl in current_rule[0]],
                [get_possibilites(rules, rules[rl]) for rl in current_rule[1]])

def get_all_possible(current, options=['']):
    if type(current) == str:
        return [prv+current for prv in options]
    elif type(current) == list:
        for e in current:
            options = get_all_possible(e, options)
        return options
    elif type(current) == tuple:
        return get_all_possible(current[0], options) + get_all_possible(current[1], options)


# PART 2
def get_results_2(data):
    rules, messages = get_data(data)
    # rules[8] = ([42], [42, 8])
    # rules[11] = ([42, 31], [42, 11, 31])
    print(rules)
    checked = []
    for msg in messages:
        val, chr = validate_char(rules, rules[0], msg)
        print(f'{msg} was {val} ended at {chr} ? {len(msg)}')
        if val:
            checked.append(val)
    # possibilities = get_possibilites(rules, rules[0])
    # print(possibilities)
    # valid_options = get_all_possible(possibilities)
    # print(f'valid_options {len(valid_options)}\n ')
    # print(f'is set {len(valid_options) == len(set(valid_options))} {len(valid_options)=}')
    # print(f'{len(max(valid_options))=} {len(min(valid_options))=}')
    # print(f'{len(max(messages))=} {len(min(messages))=}\n')
    # checked = [msg for msg in messages if msg in valid_options]
    print('checked')
    print(checked,'\n')
    return len(checked)


def validate_word(rules, curr_rule, word):
    pass


def validate_char(rules, curr_rule, word, curr_char=0):
    print(curr_rule, word, curr_char)
# try:
    if type(curr_rule) == str:
        return curr_rule == word[curr_char], curr_char
    elif type(curr_rule) == list:
        chars = []
        for i, rl in enumerate(curr_rule):
            val, curr_char = validate_char(rules, rules[rl], word, curr_char+i)
            chars.append(val)

        return all(chars), curr_char
    elif type(curr_rule) == tuple:
        branch = []
        for curr in curr_rule:
            chars = []
            for i, rl in enumerate(curr):
                val, curr_char = validate_char(rules, rules[rl], word, curr_char+i)
                chars.append(val)
            branch.append(all(chars))
        return any(branch), curr_char+i
    # except IndexError:
    #     return False, curr_char


def main():
    data = list(open('test1.txt', 'r'))
    print('Part ONE')
    print(f'{get_results(data)}')
    print('Part TWO')
    print(f'{get_results_2(data)}')


if __name__ == "__main__":
    main()
