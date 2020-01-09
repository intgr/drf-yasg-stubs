from setuptools import setup

setup(
    name="drf-yasg-stubs",
    version="0.0.1",
    description="Typing stubs for drf-yasg library (PEP 484 stubs for Mypy and PyCharm)",
    license="MIT",
    url="https://github.com/intgr/drf-yasg-stubs",
    author="Marti Raudsepp",
    author_email="marti@juffo.org",
    python_requires=">=3.6",
    install_requires=["drf-yasg"],
    packages=["drf_yasg-stubs"],
    package_data={"drf_yasg-stubs": ["*.pyi"]},
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
)
