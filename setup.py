# coding: utf-8
import os

import setuptools

import pylf


def main():
    setuptools.setup(
        name="pylf",
        version=pylf.__version__,
        description="A lightweight Python library for simulating Chinese handwriting",
        license="bsd-3-clause",
        author="Gsllchb",
        author_email="Gsllchb@gmail.com",
        python_requires=">= 3.5",
        keywords="simulating Chinese handwriting",
        url="https://github.com/Gsllchb/PyLf",
        long_description_content_type="text/markdown",
        long_description=get_long_description(),
        zip_safe=True,
        packages=setuptools.find_packages(exclude=("*.tests", "tests")),
        classifiers=(
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: Implementation :: CPython",
            "Programming Language :: Python :: Implementation :: PyPy",
        ),
        install_requires=(
            "pillow >= 5.2.0, < 6",
            "pyyaml >= 3.13, < 5",
        ),
        setup_requires=(
            "setuptools>=38.6.0",
        ),
        entry_points={
            "console_scripts": ("pylf = pylf.__main__:main",),
        }
    )


def get_long_description() -> str:
    with open(abs_path("README.md"), encoding="utf-8") as f:
        return f.read()


def abs_path(path: str) -> str:
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), path)


if __name__ == "__main__":
    main()
