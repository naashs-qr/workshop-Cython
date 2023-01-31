import setuptools
from Cython.Build import cythonize

if __name__ == '__main__':
    setuptools.setup(
        ext_modules= cythonize(
            "./demo/cython/*.pyx",
            annotate=True,
        ),
        package_data={
            'demo': ['./demo/cython/*']
        }
    )
