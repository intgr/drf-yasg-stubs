import os
from typing import List

from setuptools import setup

with open("README.md") as f:
    readme = f.read()


def find_stub_files(name: str) -> List[str]:
    """
    It seems setuptools does not support recursive patterns.

    This function is stolen from django-stubs project :)
    """
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


setup(
    name="drf-yasg-stubs",
    version="0.1.3",
    description="Typing stubs for drf-yasg library (PEP 484 stubs for Mypy and PyCharm)",
    license="MIT",
    url="https://github.com/intgr/drf-yasg-stubs",
    author="Marti Raudsepp",
    author_email="marti@juffo.org",
    long_description=readme,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    install_requires=[],
    packages=["drf_yasg-stubs"],
    package_data={"drf_yasg-stubs": find_stub_files("drf_yasg-stubs")},
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)
