import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mt_utils",
    version="0.0.1",
    author="Mirko Thalmann",
    author_email="mirkothalmann@hotmail.com",
    description="Mirko Thalmann's utility functions for everyday python use",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MirkoTh/mt_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
