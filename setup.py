import os

from setuptools import setup

consts = {}
with open(os.path.join("ostrom", "const.py")) as fp:
    exec(fp.read(), consts)

setup(
    name="pyOstrom",
    packages=["ostrom"],
    install_requires=[
        "aiohttp>=3.0.6",
        "gql[websockets]>=3.0.0",
    ],
    package_data={"ostrom": ["py.typed"]},
    version=consts["__version__"],
    description="A python3 library to communicate with Ostrom",
    python_requires=">=3.11.0",
    author="Matthias Füg",
    url="https://github.com/MFueg/pyOstrom",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
