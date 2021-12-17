# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='test', 
    version='0.1',
    description='test package',
    author='test1234',
    author_email='test1234@email.re.kr',
    long_description=long_description,
    python_requires='>=3.6',
    long_description_content_type="text/markdown",
    packages= find_packages(exclude = ['docs', 'tests*','__pycache__/']),
)