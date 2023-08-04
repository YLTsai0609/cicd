from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

try:
    with open(path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = f.read()
except:
    long_description = ""

setup(
    name="cicd",  # Required
    version="0.1",  # Required
    description="yu long's playground of cicd",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    author="yltsai0609",  # Optional
    author_email="yltsai0609@gmail.com",  # Optional
    packages=["cicd"],
)
