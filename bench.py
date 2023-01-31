import timeit

def main():
    # TODO: use timeit.timeit to compare execution time of python and cython
    # code snippet you might need to use the extra argument "setup=" :)
    cloopT = timeit.timeit('cloop(50)', setup='from demo.cython.demo import cloop')
    pyloopT = timeit.timeit('pyloop(50)', setup='from demo.demo import pyloop')
    ccountT = timeit.timeit('ccount(10)', setup='from demo.cython.demo import ccount')
    pycountT = timeit.timeit('pycount(10)', setup='from demo.demo import pycount')
    betterccountT = timeit.timeit('betterccount(10)', setup='from demo.cython.demo import betterccount')

    loopR = pyloopT / cloopT
    countR = pycountT / ccountT
    betterccountR = pycountT / betterccountT

    print(f"Loop: {pyloopT:.2f}s / {cloopT:.2f}s = {loopR:.2f}")
    print(f"Count: {pycountT:.2f}s / {ccountT:.2f}s = {countR:.2f}")
    print(f"Better Count: {pycountT:.2f}s / {betterccountT:.2f}s = {betterccountR:.2f}")

if __name__ == '__main__':
    main()
