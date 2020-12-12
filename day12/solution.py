from collections import deque

CARDIN = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
COMPASS = ((1, 0), (0, 1), (-1, 0), (0, -1))
FORWARD = 'F'
TURN = {'L': -1, 'R': 1}


def get_manhattan(data):
    location = [0, 0]
    direction = 1
    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])
        if action in CARDIN.keys():
            location = [prev + new*value for prev, new in zip(location, COMPASS[CARDIN[action]])]
        elif action == FORWARD:
            location = [prev + new*value for prev, new in zip(location, COMPASS[direction])]
        elif action in TURN.keys():
            direction = (direction + (value//90)*TURN[action]) % 4
        else:
            raise Exception('SOMETHING FAILED')
    return abs(location[0]) + abs(location[1])


def get_manhattan_waypoint(data):
    location = [0, 0]
    waypoint = [1, 10]

    for instruction in data:
        action = instruction[0]
        value = int(instruction[1:])
        if action in CARDIN.keys():
            waypoint = [prev + new*value for prev, new in zip(waypoint, COMPASS[CARDIN[action]])]
        elif action == FORWARD:
            location = [prev + new*value for prev, new in zip(location, waypoint)]
        elif action in TURN.keys():
            #                 N  E  S  W
            rotation = deque([0, 0, 0, 0])
            # Get North / South
            if waypoint[0] >= 0:
                rotation[0] = waypoint[0]
            else:
                rotation[2] = abs(waypoint[0])
            # Get East / West
            if waypoint[1] >= 0:
                rotation[1] = waypoint[1]
            else:
                rotation[3] = abs(waypoint[1])
            rotation.rotate((value//90)*TURN[action])
            waypoint[0] = rotation[0] - rotation[2]
            waypoint[1] = rotation[1] - rotation[3]
        else:
            raise Exception('SOMETHING FAILED')

    return abs(location[0]) + abs(location[1])


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [row.strip() for row in puzzle_input]
    print('Part ONE')
    print(f'{get_manhattan(data)}')
    print('Part TWO')
    print(f'{get_manhattan_waypoint(data)}')


if __name__ == "__main__":
    main()
