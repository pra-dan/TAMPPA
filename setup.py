import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TAMPPA-pra-dan",
    version="0.0.1",
    author="Prashant Dandriyal",
    author_email="prashantdandriyal7@gmail.com",
    description="Timing And Memory Profile Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pra-dan/TAMPPA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
