import setuptools
from Cython.Build import cythonize

if __name__ == '__main__':
    #TODO let's setup our module cython as a package to be recovered in other files
    setuptools.setup(
        ext_modules=cythonize('./demo/cython/demo.pyx', annotate = True),
        package_data={
            'demo': ['demo/cython/*']
        }
    )
