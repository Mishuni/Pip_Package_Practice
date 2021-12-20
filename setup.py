# Pip_Package_Practice/setup.py
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

username = "username"
setup(
    name='test_%s'%username, 
    version='0.1.1',
    author='test1234',
    author_email='test1234@email.re.kr',
    description='test package',
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
)