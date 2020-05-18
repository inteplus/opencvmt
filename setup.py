#!/usr/bin/env python3

from setuptools import setup, find_packages, find_namespace_packages
from mt.opencv.version import version

setup(name='opencvmt',
      version=version,
      description="Minh-Tri Pham's extra modules using OpenCV",
      author=["Minh-Tri Pham"],
      packages=find_packages() + find_namespace_packages(include=['mt.*']),
      install_requires=[
          'basemt>=0.3.0',
          # opencv is detected at run-time for flexibility
      ]
      )
