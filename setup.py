import os
import platform
import sys

from setuptools import setup, find_packages

setup(
    version="1.0",
    name="converter",
    packages=find_packages(),
    py_modules=["converter"],
    license="MIT",
    author="Skiniya",
    install_requires=['faster-whisper', 'pydub', 'tqdm'],
    description="Automatically generate text into your audio",
    entry_points={
        'console_scripts': ['converter=converter.main:main'],
    },
    include_package_data=True,
)