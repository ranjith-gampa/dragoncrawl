#!/usr/bin/env python3
"""
Setup configuration for DragonCrawl AI-powered mobile testing framework.
"""

from pathlib import Path
from setuptools import setup, find_packages

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

# Read requirements
requirements_file = Path(__file__).parent / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#")
        ]

# Read development requirements
dev_requirements_file = Path(__file__).parent / "requirements-dev.txt"
dev_requirements = []
if dev_requirements_file.exists():
    with open(dev_requirements_file, "r", encoding="utf-8") as f:
        dev_requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#")
        ]

setup(
    name="dragoncrawl",
    version="0.1.0",
    author="DragonCrawl Team",
    author_email="team@dragoncrawl.ai",
    description="AI-Powered Mobile Testing Framework using Language Generation Models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ranjith-gampa/dragoncrawl",
    project_urls={
        "Bug Tracker": "https://github.com/ranjith-gampa/dragoncrawl/issues",
        "Documentation": "https://dragoncrawl.readthedocs.io/",
        "Source Code": "https://github.com/ranjith-gampa/dragoncrawl",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Framework :: FastAPI",
        "Framework :: Pytest",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "docs": [
            "sphinx>=7.2.0",
            "sphinx-rtd-theme>=1.3.0",
            "sphinx-autodoc-typehints>=1.25.0",
        ],
        "gpu": [
            "torch[cuda]>=2.1.0",
            "faiss-gpu>=1.7.4",
        ],
        "ios": [
            "tidevice>=0.9.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "dragoncrawl=dragoncrawl.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "dragoncrawl": ["py.typed"],
    },
    zip_safe=False,
    keywords=[
        "mobile testing",
        "ai testing",
        "language models",
        "test automation",
        "mpnet",
        "transformers",
        "appium",
        "selenium",
        "fastapi",
    ],
)