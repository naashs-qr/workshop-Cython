import timeit

def main():
    cloopT = timeit.timeit(
        'cloop(50)',
        setup="from demo.cython.demo import cloop"
    )
    pyloopT = timeit.timeit(
        'pyloop(50)',
        setup="from demo.demo import pyloop"
    )
    ccountT = timeit.timeit(
        'ccount(10)',
        setup="from demo.cython.demo import ccount"
    )
    pycountT = timeit.timeit(
        'pycount(10)',
        setup="from demo.demo import pycount"
    )

    loopR = pyloopT / cloopT
    countR = pycountT / cloopT

    print(f"Loop: {pyloopT:.2f}s / {cloopT:.2f}s = {loopR:.2f}")
    print(f"Count: {pycountT:.2f}s / {ccountT:.2f}s = {countR:.2f}")

if __name__ == '__main__':
    main()
