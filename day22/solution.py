from collections import deque


def get_data(data):
    data = [l.strip() for l in data]
    player_1 = data[1:len(data)//2]
    player_2 = data[len(data)//2+2:]
    player_1 = deque([int(n) for n in player_1])
    player_2 = deque([int(n) for n in player_2])
    return player_1, player_2


# PART 1
def crab_combat(data):
    player_1, player_2 = get_data(data)
    # PLAY
    while len(player_1) > 0 and len(player_2) > 0:
        if player_1[0] > player_2[0]:
            arrange_deques(player_1, player_2)
        else:
            arrange_deques(player_2, player_1)

    winner = player_1 if len(player_1) > 0 else player_2
    return get_score(winner)


def arrange_deques(winner, looser):
    winner.rotate(-1)
    winner.append(looser.popleft())
    return winner, looser


def get_score(winner):
    winner.reverse()
    score = 0
    for x, n in enumerate(winner, 1):
        score += n*x
    return score


# PART 2
def recursive_combat(player_1, player_2, recursive=False):
    # PLAY
    previous_rounds = []
    winner = None
    while len(player_1) > 0 and len(player_2) > 0:
        # CHECK PREVIOUS ROUNDS
        current_round = ([c for c in player_1], [c for c in player_2])
        if current_round in previous_rounds:
            winner = player_1
            if recursive:
                return True
            break
        else:
            previous_rounds.append(current_round)

        player_1_draw = player_1[0]
        player_2_draw = player_2[0]
        # RECURSIVE GAME
        if player_1_draw < len(player_1) and player_2_draw < len(player_2):
            if recursive_combat(deque([c for c in list(player_1)[1:player_1_draw+1]]),
                                deque([c for c in list(player_2)[1:player_2_draw+1]]),
                                True):
                # player 1 wins recursive game
                arrange_deques(player_1, player_2)
            else:
                # player 2 wins recursive gane
                arrange_deques(player_2, player_1)

        # NORMAL GAME
        elif player_1_draw > player_2_draw:
            # player 1 wins by high card
            arrange_deques(player_1, player_2)
        else:
            # player 2 wins by high card
            arrange_deques(player_2, player_1)

    if recursive:
        return len(player_1) > 0

    if not winner:
        winner = player_1 if len(player_1) > 0 else player_2
    return get_score(winner)


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{crab_combat(data)}')
    print('Part TWO')
    player_1, player_2 = get_data(data)
    print(f'{recursive_combat(player_1, player_2)}')


if __name__ == "__main__":
    main()
