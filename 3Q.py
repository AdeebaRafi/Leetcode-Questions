import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for _ in range(T):
        N = int(sys.stdin.readline())
        blocks = []
        for _ in range(N):
            C, k, l, m = map(int, sys.stdin.readline().split())
            area = (l - C) * (m - k)
            center_x = (C + l) / 2
            center_y = (k + m) / 2
            blocks.append({'C': C, 'k': k, 'l': l, 'm': m, 'area': area, 'center_x': center_x, 'center_y': center_y})

        ancestor = [-1] * N
        descendants = [[] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if blocks[i]['k'] == blocks[j]['m']:  # i sits on top of j
                    if not (blocks[i]['l'] <= blocks[j]['C'] or blocks[i]['C'] >= blocks[j]['l']):
                        ancestor[i] = j
                        descendants[j].append(i)
                        break

        is_stable = True

        def compute(u):
            nonlocal is_stable
            sum_mass = blocks[u]['area']
            sum_cx = blocks[u]['area'] * blocks[u]['center_x']
            sum_cy = blocks[u]['area'] * blocks[u]['center_y']
            for v in descendants[u]:
                mass_v, cx_v, cy_v = compute(v)
                sum_mass += mass_v
                sum_cx += mass_v * cx_v
                sum_cy += mass_v * cy_v
            if ancestor[u] != -1:
                par = ancestor[u]
                final_cx = sum_cx / sum_mass
                if not (blocks[par]['C'] <= final_cx <= blocks[par]['l']):
                    is_stable = False
            return sum_mass, sum_cx / sum_mass, sum_cy / sum_mass

        for i in range(N):
            if ancestor[i] == -1 and blocks[i]['k'] == 0:
                compute(i)
        print("Stable" if is_stable else "Unstable")

threading.Thread(target=main).start()
