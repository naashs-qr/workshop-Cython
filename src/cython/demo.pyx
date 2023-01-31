# distutils: language=c++
# cython: language_level=3
def cloop(count=50):
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
    cdef int result = 0
    cdef int a = 0
    cdef int b = 0
    cdef int c = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break
                if c * c == (a * a + b * b):
                    result += 1
    return result