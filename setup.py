import setuptools
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="TAMPPA-pra-dan",
    #version=versioneer.get_version(),
    version="0.0.1",
    #cmdclass=versioneer.get_cmdclass(),
    author="Prashant Dandriyal",
    author_email="prashantdandriyal7@gmail.com",
    description="Time And Memory Profile Parser",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pra-dan/TAMPPA",
    license="MPL",
    keywords=['memory','parsing','parser','timing', 'timer', 'profiling', 'profiler', 'line_profiler'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=requirements,
)
