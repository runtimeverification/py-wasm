#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import (
    setup,
    find_packages,
)

extras_require = {
    'test': [
        "pytest>=7.4.3,<8",
        "pytest-watch>=4.2.0,<5",
        "pytest-xdist>=3.2.0,<4",
        "tox>=4.11.3,<5",
        "hypothesis>=6.88.1,<7",
    ],
    'lint': [
        "flake8==3.6.0",
        "isort>=4.3.9,<5",
        "mypy==1.6.1",
    ],
    'doc': [
        "Sphinx>=1.6.5,<2",
        "sphinx_rtd_theme>=0.1.9",
    ],
    'dev': [
        "bumpversion>=0.5.3,<1",
        "pytest-watch>=4.1.0,<5",
        "wheel",
        "twine",
        "ipython",
    ],
}

extras_require['dev'] = (
    extras_require['dev']
    + extras_require['test']  # noqa: W503
    + extras_require['lint']  # noqa: W503
    + extras_require['doc']  # noqa: W503
)

setup(
    name='py-wasm',
    # *IMPORTANT*: Don't manually change the version here. Use `make bump`, as described in readme
    version='0.2.0',
    description="""py-wasm: A python implementation of the web assembly interpreter""",
    author='Jason Carver',
    author_email='ethcalibur+pip@gmail.com',
    url='https://github.com/ethereum/py-wasm',
    include_package_data=True,
    install_requires=[
        "mypy_extensions>=1.0.0",
        "numpy>=1.16.0,<2",
        "toolz>0.9.0,<1;implementation_name=='pypy'",
        "cytoolz>=0.9.0,<1.0.0;implementation_name=='cpython'",
    ],
    python_requires='>=3.5, <4',
    extras_require=extras_require,
    py_modules=['wasm'],
    license="MIT",
    zip_safe=False,
    keywords='ethereum',
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
