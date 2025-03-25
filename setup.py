from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_desc = f.read()

with open("requisitos.txt") as f:
    requisitos = f.read().splitlines()

setup(
    name="image_processing",
    version="0.0.1",
    author="Silas",
    url="https://github.com/Kiamisa/image-processing-package",
    packages=find_packages(),
    install_requires=requisitos,
    python_requires = '>-3.11'
)
