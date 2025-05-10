from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ddnet_parser",
    version="1.0.1-dev",
    author="neyxezz",
    author_email="bassboosthelp@gmail.com",
    description="Простой парсер данных с различных сайтов дднета",
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
