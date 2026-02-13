import random

# setup game
def setup_game():
    numbers = list(range(1, 21))   # 1 to 20
    random.shuffle(numbers)

    # each player gets 20 numbers from 1–20
    players = {f"P{i}": random.sample(range(1, 21), 20) for i in range(1,6)}

    cuts = {p:0 for p in players}

    return numbers, players, cuts


# check if number matches
def check_number(players, cuts, n):
    for p in players:
        if n in players[p]:
            players[p].remove(n)
            cuts[p] += 1
            print(p, "cut!", cuts[p])

            if cuts[p] == 5:
                return p
    return None
