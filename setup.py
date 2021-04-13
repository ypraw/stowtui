from inspect import getsource

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setup(
    name="stowtui",
    version='1.1.3',
    # Get the description from second line & remove `*` character
    description="stow tui is a Terminal User Interface Program for GNU STOW",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ypraw/stowtui",
    author="Yunindyo Prabowo",
    author_email="Yunindyo.prabowo@gmail.com",
    python_requires=">=3.6",
    license="gpl-3.0",
    install_requires=["npyscreen"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    scripts=['bin/stowtui'],
    keywords="stowtui stow dotfiles tui",
)
