from setuptools import setup

setup(
    name='my_package',
    version='0.0.1',
    description='My package from github repo',
    url='git@github.com:TotalDwarf03/python-package-test.git',
    author='Kieran Pritchard',
    license='unlicense',
    packages=['test_module', 'addition_module'],
    zip_safe=False
)