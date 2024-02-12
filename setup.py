from setuptools import setup, find_packages

VERSION = "0.0.3"
DESCRIPTION = "A small package that simplifies tkinter grids"

setup(
    name="tkgrider",
    version=VERSION,
    description=DESCRIPTION,
    author="oivalian",
    packages=find_packages(),
    install_requires=[
        "ttkbootstrap",
    ],
)
