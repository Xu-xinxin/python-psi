# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="delta_psi",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    exclude_package_data={'': ['.gitignore']},
    install_requires=[
        'numpy~=1.20.2',
        'pycryptodome~=3.10.1'
    ],
    zip_safe=False,
    author="miaohong",
    author_email="miaohong@yuanben.org",
    description="package for private set intersection",
    python_requires='>=3.6',
)
