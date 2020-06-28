import os

from setuptools import setup, find_packages

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
PACKAGE_NAME = "gradgpad"
VERSION = open("gradgpad/VERSION", "r").read()

# The text of the README file
with open(os.path.join(CURRENT_DIR, "README.md")) as fid:
    README = fid.read()

with open("requirements/requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description="gradgpad",
    long_description=README,
    long_description_content_type="text/markdown",
    keywords=["face-PAD", "framework", "evaluation"],
    url="https://github.com/acostapazo/gradgpad",
    author="ALiCE Biometrics",
    author_email="acosta@alicebiometrics.com",
    license="MIT",
    install_requires=required,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(exclude=("tests*",)),
    include_package_data=True,
    zip_safe=False,
)
