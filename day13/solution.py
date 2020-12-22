def get_bus(data):
    timestamp = int(data[0])
    buses = [int(bus.strip()) for bus in data[1].split(',') if bus != 'x']
    buses_times = []
    for bus in buses:
        buses_times.append(bus - timestamp % bus)
    best_bus = buses[buses_times.index(min(buses_times))]
    return ((timestamp // best_bus + 1)*best_bus - timestamp) * best_bus

# 
# def get_bus2(data):
#     buses = [(int(bus.strip()), i) for i, bus in enumerate(data[1].split(',')) if bus != 'x']
#     print(buses)
#     inc = buses[0][0]
#     while True:
#         check = []
#         for bus_data in buses:
#             bus, index = bus_data
#             check.append((inc + index) % bus == 0)
#         if all(check):
#             return f'{int(data[0]) == inc} {inc =}'
#         inc += buses[0][0]
#     return None


def main():
    puzzle_input = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_bus(puzzle_input)}')
    # print('Part TWO')
    # print(f'{get_bus2(puzzle_input)}')


if __name__ == "__main__":
    main()
