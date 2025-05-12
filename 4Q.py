# This is a sample Python script.

def min_actions_to_visit_buttons(T, t_case):
    results = []
    for case in t_case:
        N, M, grid = case
        pos = {}
        for r in range(N):
            for c in range(M):
                pos[grid[r][c]] = (r, c)

        actions = 0
        currentt_r, current_c = 0, 0

        for num in range(1, N * M + 1):
            targeet_r, target_c = pos[num]
            vert_move = min(abs(currentt_r - targeet_r), N - abs(currentt_r - targeet_r))
            hori_move = min(abs(current_c - target_c), M - abs(current_c - target_c))
            actions += vert_move + hori_move
            currentt_r, current_c = targeet_r, target_c

        results.append(actions)
    return results


T = int(input())
t_case = []
for _ in range(T):
    N, M = map(int, input().split())
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
    t_case.append((N, M, grid))

answers = min_actions_to_visit_buttons(T, t_case)

for answer in answers:
    print(answer)
