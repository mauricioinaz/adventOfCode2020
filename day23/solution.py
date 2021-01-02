from collections import deque


# PART 1
def crab_cups(data):
    circle = list(data.strip())
    moves = 0
    while moves < 10000000:
        # pickup next three after current
        pickup = []
        for _ in range(3):
            pickup.append(circle.pop(1))

        # find destination cup
        sorted_circle = sorted([v for v in circle])
        current_indx_in_sorted = sorted_circle.index(circle[0])
        dest_cup = sorted_circle[current_indx_in_sorted-1]
        dest_cup_indx = circle.index(dest_cup)

        # insert pickup after destination
        for _ in range(3):
            circle.insert(dest_cup_indx+1, pickup.pop())

        # rearrange circle
        dq = deque(circle)
        dq.rotate(-1)
        circle = list(dq)

        moves += 1

    # get order of circle using 1 as reference
    position_1 = circle.index('1')
    result = deque(circle)
    result.rotate(-position_1-1)
    result.pop()  # eliminate 1
    return ''.join(result)


def main():
    data = list(open('input.txt', 'r'))[0]
    print('Part ONE')
    print(f'{crab_cups(data)}')


if __name__ == "__main__":
    main()
