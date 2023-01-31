import setuptools
from Cython.Build import cythonize

if __name__ == '__main__':
    setuptools.setup(
        ext_modules=cythonize('src/cython/*.pyx', annotate=True),
        package_data={
            'demo': [
                'src/cython/demo.cpp'
            ]
        }
    )