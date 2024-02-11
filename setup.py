from setuptools import setup, find_packages
setup(
name='siconv',
version='0.1.0',
author='sahan ruwantha',
author_email='sahanr.silva@proton.me',
description='''The siconv Python package simplifies the conversion between Sinhala and Singlish languages. Whether you're dealing with Sinhala text that needs transformation into Singlish or vice versa, siconv offers a user-friendly solution.Resources''',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: GNU GENERAL PUBLIC LICENSE',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)