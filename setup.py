# !/usr/bin/env python3
# coding:utf-8
"""
Name       : setup.py
Author     : Kuldeep Singh Sidhu
Time       : 27-11-2020 02:58 PM
GitHub     : https://github.com/singhsidhukuldeep
Description: Used to setup stay-awake
"""

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python',

]

setup(
    name='stay-awake',
    version='0.3',
    description='Simple Platform Independent Python package to keep your system awake without affecting workflow!',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read()+'\n\nRead more at https://github.com/singhsidhukuldeep/stay-awake',
    long_description_content_type="text/markdown",
    url='https://github.com/singhsidhukuldeep/stay-awake',
    author='Kuldeep Singh Sidhu',
    author_email='singhsidhukuldeep@gmail.com',
    classifiers=classifiers,
    keywords='stay awake',
    packages=find_packages(),
    install_requires=['pyautogui', 'tqdm'],
    zip_safe=False,
)