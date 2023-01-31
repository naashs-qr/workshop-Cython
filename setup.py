import setuptools
from Cython.Build import cythonize

if __name__ == '__main__':
    setuptools.setup(
        ext_modules=cythonize("demo/cython/demo.pyx"),
        packages=['demo', 'demo.cython'],
        package_data={
            'demo': ['*.py'],
            'demo.cython': ['*.pyx']
        }
    )
