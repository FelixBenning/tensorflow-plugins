from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read() 

setup(
    name="tensorflow-plugins",
    version="0.1",
    description="Demo how Optimizers, Models, Loss functins, etc. might be grouped",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["tf_plugins"],
    install_requires=[
        "tensorflow~=2.5",
    ]
)
