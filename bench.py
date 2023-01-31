from sys import argv
import timeit

def main():
    pyloopT  = timeit.timeit("pyloop(50)",  setup="from demo.demo import pyloop")
    cloopT   = timeit.timeit("cloop(50)",   setup="from demo.cython.demo import cloop")
    pycountT = timeit.timeit("pycount(10)", setup="from demo.demo import pycount")
    ccountT  = timeit.timeit("ccount(10)",  setup="from demo.cython.demo import ccount")
    print (f"Functions\t\t| Cy(sec)\t| Py(sec)\t| Py/Cy")
    print (f"cloop vs pyloop  \t| {cloopT:.3f}\t| {pyloopT:.3f}\t| {pyloopT/cloopT:.2f}")
    print (f"ccount vs pycount\t| {ccountT:.3f}\t| {pycountT:.3f}\t| {pycountT/ccountT:.2f}")
    if len(argv) != 0:
        bettercountT = timeit.timeit("betterccount(10)", setup="from demo.cython.demo import betterccount")
        print (f"Bccount vs pycount\t| {bettercountT:.3f}\t| {pycountT:.3f}\t| {pycountT/bettercountT:.2f}")

    

if __name__ == '__main__':
    main()