# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

username = "username"
setup(
    name='test_%s'%username, # Required
    version='0.1.2', # Required
    description='test package',# Required
    author='test1234',
    author_email='test1234@email.re.kr',
    long_description=long_description,
    python_requires='>=3.6',
    long_description_content_type="text/markdown",
    #packages= find_packages(include=['test_package', 'test_package.*'],exclude = ['docs', 'tests*','__pycache__/']),
    packages= find_packages(exclude = ['docs', 'tests*','__pycache__/']),
    url="https://github.com/Mishuni/Pip_Package_Practice.git",
    install_requires=[
        ''
    ],
    entry_points={
        'console_scripts': [
            'test-main=test_package.__main__:main',
            'tpm=test_package.__main__:main',
        ],
    },
    license='MIT',
    keywords = "test sample",
    classifiers=["Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: 3.6",
                 "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"],
    
)