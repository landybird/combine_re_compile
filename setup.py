# encoding : utf-8
# __author__ = 'jm'

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="combine_re_compile",  #
    version="0.0.2",
    author="landybird",
    author_email="1442172978@qq.com",
    description="combine re compile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/landybird/combine_re_compile",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)