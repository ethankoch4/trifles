import os
from distutils.core import setup

with open(os.path.join('.', 'README.md'), 'r') as long_f:
    long_description = long_f.read()

setup(
    name='trifles',
    version='0.0.1',
    description='Python library for Algorithms and Data Structures.',
    author='Ethan Koch',
    author_email='ethankoch4@gmail.com',
    maintainer='Ethan Koch',
    maintainer_email='ethankoch4@gmail.com',
    url='https://github.com/ethankoch4/trifles',
    packages=['trifles'],
    long_description=long_description,
    keywords=['algorithms', 'data sctructures'],
)
