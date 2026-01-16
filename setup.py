from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="water-quality-ai-system",
    version="0.1.0",
    author="Computer Science Student",
    author_email="your.email@example.com",
    description="AI-powered water quality monitoring and contamination prediction system for SDG 6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/panchanansahoo/water-quality-ai-system",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.100.0",
        "uvicorn[standard]>=0.23.0",
        "pydantic>=2.0",
        "pandas>=2.0",
        "numpy>=1.24",
        "scikit-learn>=1.3",
        "langchain>=0.1.0",
    ],
)
