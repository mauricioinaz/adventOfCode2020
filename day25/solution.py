# PART 1
def combo_break(data):
    subject_card = int(data[0])
    subject_door = int(data[1])
    loop_card = get_loop_size(subject_card)
    # loop_door = get_loop_size(subject_door)
    encryption = 1
    for _ in range(loop_card):
        encryption = encryption*subject_door % 20201227
    return encryption


def get_loop_size(target, subject=7):
    value = 1
    loop = 0
    while value != target:
        value = value*subject % 20201227
        loop += 1
    return loop


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{combo_break(data)}')


if __name__ == "__main__":
    main()
