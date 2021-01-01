from collections import deque


def get_data(data):
    data = [l.strip() for l in data]
    player_1 = data[1:len(data)//2]
    player_2 = data[len(data)//2+2:]
    player_1 = deque([int(n) for n in player_1])
    player_2 = deque([int(n) for n in player_2])
    return player_1, player_2


# PART 1
def get_score(data):
    player_1, player_2 = get_data(data)
    # PLAY
    while len(player_1) > 0 and len(player_2) > 0:
        if player_1[0] > player_2[0]:
            player_1, player_2 = arrange_deques(player_1, player_2)
        else:
            player_2, player_1 = arrange_deques(player_2, player_1)

    # GET SCORE
    winner = player_1 if len(player_1) > 0 else player_2
    winner.reverse()
    score = 0
    for x, n in enumerate(winner, 1):
        score += n*x
    return score


def arrange_deques(winner, looser):
    winner.rotate(-1)
    winner.append(looser.popleft())
    return winner, looser


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_score(data)}')


if __name__ == "__main__":
    main()
