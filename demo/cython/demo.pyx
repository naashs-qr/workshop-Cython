# distutils: language=c++
# cython: language_level=3

def cloop(int count=50):
    res = []
    for n in range(0, count):
        res.append('Loop %d' % n)
    return '\n'.join(res)

def ccount(limit):
    result = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break
                if c * c == (a * a + b * b):
                    result += 1
    return result

def betterccount(limit):
    cdef int i, j, k
    cdef int sum = 0
    for i in range(1, limit+1):
        for j in range(i+1, limit+1):
            for k in range(j+1, limit+1):
                if k*k > i*i + j*j:
                    break
                if k*k == (i*i + j*j):
                    sum += 1
    return sum
