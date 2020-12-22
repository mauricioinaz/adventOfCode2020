CMND = 'CMND'
MEMRY = 'MEMRY'
VALUE = 'VALUE'


# DATA CLEANUP
def get_program(data):
    program_raw = [[x.strip() for x in row.split('=')] for row in data]
    program = []
    for row in program_raw:
        cmnd_data = row[0].split('[')
        command = cmnd_data[0]
        memory = None
        if len(cmnd_data) == 2:
            memory = cmnd_data[1][:-1]
        program.append({CMND: command, MEMRY: memory, VALUE: row[1]})
    return program


# PART 1
def get_version1(data):
    program = get_program(data)
    memory = {}
    mask_A = None
    mask_B = None
    for line in program:
        if line[CMND] == 'mask':
            mask_A = int(''.join(['1' if x == 'X' else '0' for x in line[VALUE]]), 2)
            mask_B = int(''.join([str(x) if x != 'X' else '0' for x in line[VALUE]]), 2)
        else:
            value = int(line[VALUE]) & mask_A
            value |= mask_B
            memory[line[MEMRY]] = value
    return sum(memory.values())


# PART 2
def get_version2(data):
    program = get_program(data)
    memory = {}
    mask_A = None
    mask_B = None
    mask_raw = None
    for line in program:
        if line[CMND] == 'mask':
            mask_A = int(''.join(['1' if x == '1' else '0' for x in line[VALUE]]), 2)
            mask_B = int(''.join(['0' if x == 'X' else '1' for x in line[VALUE]]), 2)
            mask_raw = line[VALUE]
        else:
            result = int(line[MEMRY]) | mask_A
            result = result & mask_B
            addresses = get_floating_addresses(result, mask_raw)
            for address in addresses:
                memory[address] = int(line[VALUE])

    return sum(memory.values())


def get_floating_addresses(memory, float_mask):
    floats = float_mask.count('X')
    masks = []
    for number in range(2**floats):
        # Binary representation of number, inversed, in a list
        number = list(bin(number)[2:].zfill(floats)[::-1])
        tmp_mask = ['0' for _ in range(36)]
        for ind, y in enumerate(float_mask):
            if y == 'X':
                tmp_mask[ind] = number.pop()
        masks.append(int(''.join(tmp_mask), 2) | memory)
    return masks


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_version1(data)}')
    print('Part TWO')
    print(f'{get_version2(data)}')


if __name__ == "__main__":
    main()
