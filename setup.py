#!/usr/bin/env python3
"""
Setup script for Fitness Facility Finder
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="fitness-facility-finder",
    version="1.0.0",
    author="Techyz Software Solutions Private Limited",
    author_email="info@techyz.net",
    description="🏋️‍♂️ Open-source Streamlit app to find fitness facilities using Google Places API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fitness-facility-finder",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "fitness-finder=run:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["assets/*", "config/*", "docs/*"],
    },
)
