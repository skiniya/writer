import os
import platform
import sys

from setuptools import setup, find_packages

setup(
    version="1.0",
    name="converter",
    #scripts=['full.py'],
    packages=find_packages(),
    py_modules=["converter"],
    license="MIT",
    author="Skiniya",
    install_requires=['faster-whisper', 'pydub', 'tqdm'],
    description="Automatically generate text into your audio",
    entry_points={'console_scripts': ['converter=converter.full:fullAudio'], ['converter=converter.udal:Udal'],
                  },
    include_package_data=True,
)