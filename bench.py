from timeit import timeit

def main():
    cloopT = timeit('cloop(50)', setup="from demo.cython.demo import cloop")
    pyloopT = timeit('pyloop(50)', setup="from demo.demo import pyloop")
    ccountT = timeit('ccount(10)', setup="from demo.cython.demo import ccount")
    pycountT = timeit('pycount(10)', setup="from demo.demo import pycount")

    loopR = pyloopT / cloopT
    countR = pycountT / ccountT

    betterccountT = timeit('betterccount(10)', setup="from demo.cython.demo import betterccount")

    betterccountR = pycountT / betterccountT

    print(f"Loop: {pyloopT:.2f}s / {cloopT:.2f}s = ({loopR:.2f})")
    print(f"Count: {pycountT:.2f}s / {ccountT:.2f}s = ({countR:.2f})")
    print(f"Better Count: {pycountT:.2f}s / {betterccountT:.2f}s = ({betterccountR:.2f})")
    pass

if __name__ == '__main__':
    main()
