modn = 10**9 + 7

def to_idx(s):
    reslt = 0
    for ch in s:
        reslt = (reslt << 1) | (ch == 'W')
    return reslt

def shift(st, c):
    st = (st << 1) | (c == 'W')
    st &= (1 << 15) - 1
    return st

def solve_one(n, k, x, y, w1, w2, l1, l2, pats):
    basew = (w1 + w2) // 2
    basel = (l1 + l2) // 2
    st_set = set()
    patmap = {}

    for p in pats:
        idx = 0
        for ch in p:
            idx = (idx << 1) | (ch == 'W')
        patmap[idx] = (len(p), p)

    val = [0] * (1 << 15)
    for mask in range(1 << 15):
        best = 0
        for idx, (ln, pat) in patmap.items():
            if mask >> (15 - ln) == idx:
                if pat[-1] == 'W':
                    best = max(best, x)
                else:
                    best = max(best, y)
        val[mask] = best

    mat = {}
    for i in range(1 << 15):
        for c in ['W', 'L']:
            nxt = shift(i, c)
            gain = basew if c == 'W' else basel
            gain = (gain + val[nxt]) % modn
            mat[(i, nxt)] = gain

    vec = [0] * (1 << 15)
    vec[0] = 1

    def mult(v, m):
        res = [0] * (1 << 15)
        for (i, j), g in m.items():
            res[j] = (res[j] + v[i] * g) % modn
        return res

    while n:
        if n & 1:
            vec = mult(vec, mat)
        new_mat = {}
        for (i, j), g1 in mat.items():
            for (k, l), g2 in mat.items():
                if j == k:
                    new_mat[(i, l)] = (new_mat.get((i, l), 0) + g1 + g2) % modn
        mat = new_mat
        n >>= 1

    ans = 0
    for v in vec:
        ans = (ans + v) % modn
    return ans

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    x, y, w1, w2, l1, l2 = map(int, input().split())
    pats = [input().strip() for _ in range(k)]
    print(solve_one(n, k, x, y, w1, w2, l1, l2, pats))
