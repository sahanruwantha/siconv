from setuptools import setup, find_packages

with open("README.md", "r") as fh: 
    description = fh.read() 

setup(
    name='siconv',
    version='0.1.2.7',
    author='sahan ruwantha',
    author_email='sahanr.silva@proton.me',
    description='''The siconv Python package simplifies the conversion between Sinhala and Singlish languages. Whether you're dealing with Sinhala text that needs transformation into Singlish or vice versa, siconv offers a user-friendly solution.''',
    long_description=description,
    long_description_content_type="text/markdown", 
    url="https://github.com/sahanruwantha/siconv", 
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
