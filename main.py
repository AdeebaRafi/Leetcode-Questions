import sys

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        xmin = float('inf')
        xmax = -float('inf')
        ymin = float('inf')
        ymax = -float('inf')
        for _ in range(n):
            x = float(next(it))
            y = float(next(it))
            if x < xmin: xmin = x
            if x > xmax: xmax = x
            if y < ymin: ymin = y
            if y > ymax: ymax = y
        area = (xmax - xmin) * (ymax - ymin)
        out.append(f"{area:.6f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
