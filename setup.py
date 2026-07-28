from setuptools import find_packages, setup

setup(
    name="s1320176_learn",
    version="0.1.0",
    description="SE07 class work package for PyPI repository practice",
    author="Kentaro Awashima",
    packages=find_packages(include=["s1320176_learn", "s1320176_learn.*"]),
    install_requires=["pami"],
    python_requires=">=3.9",
)

