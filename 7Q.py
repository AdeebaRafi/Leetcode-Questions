def find_champion(t, match_data):
    winners = []
    for group in match_data:
        num_players, fight_names, strength = group
        players = list(zip(fight_names, strength))

        while len(players) > 1:
            next_stage = []
            for j in range(0, len(players), 2):
                f1, s1 = players[j]
                f2, s2 = players[j + 1]

                if s1 > s2:
                    next_stage.append((f1, s1 + s2))
                elif s2 > s1:
                    next_stage.append((f2, s1 + s2))
                else:
                    next_stage.append((f1 + f2, s1 + s2))
            players = next_stage

        final_winner = players[0][0]
        winners.append(final_winner)
    return winners


# Input handling
t = int(input())
match_data = []

for _ in range(t):
    num = int(input())
    fight_names = input().split()
    strength = list(map(int, input().split()))
    match_data.append((num, fight_names, strength))

result = find_champion(t, match_data)
for champ in result:
    print(champ)
