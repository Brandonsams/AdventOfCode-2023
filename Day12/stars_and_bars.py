import numpy as np

def fast_comb(n, k):
    a = np.ones((k, n-k+1), dtype=int)
    a[0] = np.arange(n-k+1)
    for j in range(1, k):
        reps = (n-k+j) - a[j-1]
        a = np.repeat(a, reps, axis=1)
        ind = np.add.accumulate(reps)
        a[j, ind[:-1]] = 1-reps[1:]
        a[j, 0] = j
        a[j] = np.add.accumulate(a[j])
    return a

fb = fast_comb(100, 4)
sb = np.empty((6, fb.shape[1]), int)
sb[0], sb[1:5], sb[5] = -1, fb, 100
result = np.diff(sb.T) - 1

print(fb)

print(result.shape)
# (3921225, 5)
print(result[::400000])
# array([[ 0,  0,  0,  0, 96],
#        [ 2, 26, 12,  8, 48],
#        [ 5, 17, 22,  7, 45],
#        [ 8, 23, 30, 16, 19],
#        [12,  2, 73,  9,  0],
#        [16,  2, 25, 40, 13],
#        [20, 29, 24,  0, 23],
#        [26, 13, 34, 14,  9],
#        [33, 50,  4,  5,  4],
#        [45, 21, 26,  1,  3]])