import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_utilities-BE", # Replace with your own username
    version="0.0.1",
    author="Example Author",
    author_email="bernard.esterhuyse@gmail.com",
    description="A small python utilities package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bernarde01/python_utilities_BE.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)