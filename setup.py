from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ddnet_parser",
    version="1.3.0",
    author="neyxezz",
    author_email="bassboosthelp@gmail.com",
    description="Simple data parser from ddnet sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neyxezz/ddnet-parser",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Public Domain",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
