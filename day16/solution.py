# DATA CLEANUP
def get_data(data):
    # Get rules
    rules = {}
    for i, r in enumerate(data):
        row = r.strip()
        # finished reading rules
        if not row:
            break
        else:
            key, values = row.split(':')
            values = values.split('or')
            values = [rl.strip() for rl in values]
            values = [[int(n) for n in rl.split('-')] for rl in values]
            rules[key] = values

    my_ticket = data[i+2].split(',')
    my_ticket = [int(v.strip()) for v in my_ticket]

    # Get Ticket values
    ticket_values = []
    for ln in data[i+5:]:
        values = ln.split(',')
        values = [int(v.strip()) for v in values]
        ticket_values.append(values)

    return rules, ticket_values, my_ticket


# PART 1
def get_valid_tickets(data):
    rules, ticket_values, my_ticket = get_data(data)
    invalid_values = []
    valid_tickets = []
    for ticket in ticket_values:
        validity = []
        for value in ticket:
            valid = any_rule(value, rules)
            validity.append(valid)
            if not valid:
                invalid_values.append(value)
        if all(validity):
            valid_tickets.append(ticket)
    return sum(invalid_values), valid_tickets, rules, my_ticket


def any_rule(value, rules):
    for line_rule in rules.values():
        valid = False
        for rule in line_rule:
            valid |= (min(rule) <= value <= max(rule))
        if valid:
            return True
    return False


# PART 2
def get_rules_order(valid_tickets, rules):
    rules_order = {}
    # find rules that apply to each column
    for i in range(len(valid_tickets[0])):
        rule_names = list(rules.keys())
        for ticket in valid_tickets:
            for name, line_rule in rules.items():
                valid = False
                for rule in line_rule:
                    valid |= (min(rule) <= ticket[i] <= max(rule))
                if not valid:
                    rule_names.remove(name)
        rules_order[i] = set(rule_names)

    # while more than one rule per column, keep making set differences of not singles columns
    while sum([len(rls) for rls in rules_order.values()]) > len(rules_order):
        singles = [rl for rl in rules_order.values() if len(rl) == 1]
        not_singles = [k for k, rl in rules_order.items() if len(rl) > 1]
        for rule in singles:
            for k in not_singles:
                rules_order[k] -= rule

    return rules_order


def get_departures(rules_order, my_ticket):
    total = 1
    for i, rule in rules_order.items():
        (name, ) = rule
        if name[:9] == 'departure':
            total *= my_ticket[i]
    return total


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    sum_of_invalids, valid_tickets, rules, my_ticket = get_valid_tickets(data)
    print(f'{sum_of_invalids}')
    print('Part TWO')
    rules_order = get_rules_order(valid_tickets, rules)
    print(f'{get_departures(rules_order, my_ticket)}')


if __name__ == "__main__":
    main()
