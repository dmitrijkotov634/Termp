import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="termp",
    version="0.2.14",
    author="dmitrijkotov",
    author_email="dmitrijkotov634@mail.ru",
    description="Draw in terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dmitrijkotov634/Termp",
    packages=setuptools.find_packages(),
    license="MIT",
    keywords="Draw in terminal",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    install_requires=[
        "termcolor",
        "pillow"
    ]
)