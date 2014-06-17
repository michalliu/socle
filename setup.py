#!/usr/bin/python
# coding: utf-8

from distutils.core import setup

setup(
    name='socle',
    author=u"Lauri Võsandi",
    author_email="lauri.vosandi@gmail.com",
    url="https://github.com/v6sa/socle",
    version='0.4',
    packages=['socle', 'socle.boards', 'socle.plugins'],
    package_data={"socle":[]},
    data_files=[
        ("", ["README.rst"]),
        ("socle.boards", ["socle/manuf"]),
    ],
    scripts = ["misc/socle"],
    license='MIT',
    long_description=open('README.rst').read(),
)
