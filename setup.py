from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '0.0.1'
DESCRIPTION = 'A helpfull python package!'
LONG_DESCRIPTION = 'A package that allows you to have simplicity and effectiveness in your projects!'

# Setting up
setup(
    name="cutepy",
    version=VERSION,
    author="Birdlinux (G. P.)",
    author_email="<prepakis.geo@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'python system Detection', 'python hex', 'python rgb', 'python hex', 'python loader', 'rich python', 'python rich', 'cutepy'],
    classifiers=[]
)
