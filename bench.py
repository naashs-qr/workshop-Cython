from timeit import timeit

def main():
    # cloopT = timeit('cloop(50)', setup='from demo.cython.demo import cloop')
    # pyloopT = timeit('pyloop(50)', setup='from demo.demo import pyloop')
    ccountT = timeit('ccount(20)', setup='from demo.cython.demo import ccount')
    pycountT = timeit('pycount(20)', setup='from demo.demo import pycount')
    bettercount = timeit('bettercount(20)', setup='from demo.cython.demo import bettercount')
    # loopR = pyloopT / cloopT
    countR = pycountT / ccountT
    # print(f"Loop: Py = {pyloopT:.2F}s / C = {cloopT:.2f}s = {loopR:.2f}")
    print(f"Count: Py = {pycountT:.2F}s / C = {ccountT:.2f}s = {countR:.2f}")
    print(f"bettercount: C = {bettercount:.2f}")
    pass

if __name__ == '__main__':
    main()
