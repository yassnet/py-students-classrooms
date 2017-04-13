import os
from setuptools import setup

# @author Yassir Aguila
# @version $Revision: 1.0 $ $Date: 2017-04-05


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="py-students-classrooms",
    version="1.2",
    author="Yassir Aguila",
    author_email="yass.net@gmail.com",
    description="Useful library made in python to handle students and classrooms",
    license="MIT",
    keywords="example geolocation util utm",
    url="https://github.com/yassnet/py-students-classrooms",
    packages=['src'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 1.2 release",
        "Topic :: Utilities",
        "License :: MIT License",
    ]
)
