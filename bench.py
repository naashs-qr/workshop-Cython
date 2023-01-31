import timeit

def main():
    cloopT = timeit.timeit('cloop(50)', setup="from demo.cython.demo import cloop")
    pyloopT = timeit.timeit('pyloop(50)', setup="from demo.demo import pyloop")

    ccountT = timeit.timeit('ccount(10)', setup="from demo.cython.demo import ccount")
    pycountT = timeit.timeit('pycount(10)', setup="from demo.demo import pycount")

    bettercountT = timeit.timeit('betterccount(10)', setup="from demo.cython.demo import betterccount")

    loopR = pyloopT / cloopT
    countR = pycountT / ccountT

    print(f"loop: Py = {pyloopT:.2f}s / C = {cloopT:.2f} = {loopR:.2f}")
    print(f"count: Py = {pycountT:.2f}s / C = {ccountT:.2f} = {countR:.2f}")
    print(f"bettercount: Py = {pycountT:.2f}s / C = {bettercountT:.2f} = {pycountT / bettercountT:.2f}")
    pass

if __name__ == '__main__':
    main()
