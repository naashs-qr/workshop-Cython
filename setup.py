import setuptools
from Cython.Build import cythonize

if __name__ == '__main__':
    setuptools.setup(
        ext_modules=cythonize(
            "demo/cython/*.pyx",
            annotate=True
        ),
        packages=['demo', 'demo.cython'],
        package_data={
            'demo': ['*.py'],
            'demo.cython': ['*.pyx']
        }
    )
