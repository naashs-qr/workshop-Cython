def pyloop(count=50):
    res = []
    for n in range(0, count):
        res.append('Loop %d' % n)
    return '\n'.join(res)
def pycount(limit):
    result = 0
    for a in range(1, limit + 1):
        for b in range(a + 1, limit + 1):
            for c in range(b + 1, limit + 1):
                if c * c > a * a + b * b:
                    break
                if c * c == (a * a + b * b):
                    result += 1
    return result