import setuptools

setuptools.setup(
    name="PyTimer", # Replace with your own username
    version="0.57721",
    author="Katharine Long",
    author_email="katharine.long@ttu.edu",
    description="Simple timer function",
    long_description="Timer utilities.",
    long_description_content_type="text/markdown",
    url="https://github.com/krlong014/PyTimer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: LGPL License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
