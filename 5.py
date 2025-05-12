t = int(input())
for _ in range(t):
    s = input().strip()
    n = len(s)

    w_ps = [0] * (n + 1)
    for i in range(n):
        w_ps[i + 1] = w_ps[i] + (1 if s[i] == 'w' else 0)

    u_idx = [i for i, ch in enumerate(s) if ch == 'u']
    tot_u = len(u_idx)
    cnt = 0

    for i in range(tot_u):
        for j in range(i + 1, tot_u):
            lb = u_idx[i] + 1
            rb = u_idx[j] - 1
            if lb <= rb:
                w_ct = w_ps[rb + 1] - w_ps[lb]
                if w_ct > 0:
                    cnt += 1

    print(cnt)
