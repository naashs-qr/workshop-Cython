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
    bccountT = timeit.timeit(
        'bettercount(10)',
        setup="from demo.cython.demo import bettercount"
    )

    loopR = pyloopT / cloopT
    countR = pycountT / cloopT
    bcountR = pycountT / bccountT

    print(f"Loop: {pyloopT:.2f}s py / {cloopT:.2f}s C = {loopR:.2f}")
    print(f"Count: {pycountT:.2f}s py / {ccountT:.2f}s C = {countR:.2f}")
    print(f"Better: {bccountT:.2f}s C")

if __name__ == '__main__':
    main()
