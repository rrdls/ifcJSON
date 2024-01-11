from setuptools import setup, find_packages

setup(
    name="ifcjson",
    version="0.1",
    packages=find_packages(),
    install_requires=["ifcopenshell", "numpy"],
)
