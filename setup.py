import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="h5pyd-pkg-sirwyver",  # Replace with your own username
    version="0.1.0.2",
    author="Norman Müller",
    author_email="norman.mueller@tum.de",
    description="h5py wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
