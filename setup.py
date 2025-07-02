from setuptools import setup, find_packages

setup(
    name="conduction_analysis",
    version="0.1.0",
    description="A toolkit for segmenting I-V data and classifying conduction mechanisms in resistive devices.",
    author="Vishal-kr6",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib"
    ],
    python_requires=">=3.7",
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)