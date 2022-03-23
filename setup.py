
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as readme:
  long_description = readme.read()

setup(
  name="winmutex",
  version="2.0.0",
  description="Home maid subsets for me which provide windows native mutex.",
  long_description=long_description,
  long_description_content_type="text/markdown",
  author="tikubonn",
  author_email="https://twitter.com/tikubonn",
  url="https://github.com/tikubonn/winmutex",
  license="MIT",
  packages=find_packages(),
  install_requires=[],
  dependency_links=[],
  entry_points={},
  classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "License :: OSI Approved :: MIT License",
  ],
  test_suite="test"
)
