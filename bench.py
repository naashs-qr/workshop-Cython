import timeit
import demo.cython.demo as cdemo
import demo.demo as pydemo


def main():
    py_time = timeit.timeit(lambda: pydemo.pyloop(),
                            number=100, setup="import demo")
    print(f"Pyloop time: {py_time:.6f} sec")

    c_time = timeit.timeit(lambda: cdemo.cloop(),
                           number=100, setup="import demo")
    print(f"Cloop time: {c_time:.6f} sec")
    print(f"Cloup is {py_time / c_time:.2f} times faster than Pyloop")

    print()

    py_count_time = timeit.timeit(lambda: pydemo.pycount(
        50), number=100, setup="import demo")
    print(f"Pycount time: {py_count_time:.6f} sec")

    c_count_time = timeit.timeit(lambda: cdemo.ccount(
        50), number=100, setup="import demo")
    print(f"Ccount time: {c_count_time:.6f} sec")
    print(
        f"Ccount is {py_count_time / c_count_time:.2f} times faster than Pycount")

    print()

    better_c_count_time = timeit.timeit(lambda: cdemo.betterccount(
        50), number=100, setup="import demo")
    print(f"Better Ccount time: {better_c_count_time:.6f} sec")
    print(
        f"Better Ccount is {py_count_time / better_c_count_time:.2f} times faster than Ccount")


if __name__ == '__main__':
    main()
