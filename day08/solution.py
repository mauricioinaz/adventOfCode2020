def extract_commands(data):
    commands = []
    for row in data:
        operation, argument = row.split()
        arg = int(argument[1:])
        if argument[0] == '-':
            arg *= -1
        commands.append([operation, arg])
    return commands


# PART 1
def check_for_loop(commands):
    i = 0
    used_indexes = []
    accumulator = 0
    while i not in used_indexes:
        used_indexes.append(i)
        # index at end
        if i == len(commands):
            return accumulator, True
        # index overflow
        elif i > len(commands):
            return 0, False
        operation, argument = commands[i]
        if operation == 'acc':
            accumulator += argument
            i += 1
        elif operation == 'nop':
            i += 1
        elif operation == 'jmp':
            i += argument

    return accumulator, False


# PART 2
def fix_code(commands):
    for i, row in enumerate(commands):
        if row[0] == 'jmp':
            # make a true copy of commands
            tmp_commands = [row[:] for row in commands]
            tmp_commands[i][0] = 'nop'
            acc, finished = check_for_loop(tmp_commands)
            if finished:
                return acc
    return None


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    commands = extract_commands(data)
    print('Part ONE')
    acc, _ = check_for_loop(commands)
    print(f'{acc}')
    print('Part TWO')
    print(f'{fix_code(commands)}')


if __name__ == "__main__":
    main()
