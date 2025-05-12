import sys
import numpy as np
from scipy.spatial import ConvexHull

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    t = int(next(it))
    out = []
    for _ in range(t):
        n = int(next(it))
        pts = np.empty((n, 3), dtype=float)
        for i in range(n):
            pts[i, 0] = float(next(it))
            pts[i, 1] = float(next(it))
            pts[i, 2] = float(next(it))
        # build the convex hull in 3D and read its volume
        hull = ConvexHull(pts)
        vol = hull.volume
        out.append(f"{vol:.2f}")
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
