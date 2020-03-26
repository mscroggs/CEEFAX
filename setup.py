from setuptools import setup

with open("README") as f:
    long_description = f.read()

with open("VERSION") as f:
    v = f.read()

setup(
   name='ceefax',
   version=v,
   description='CEEFAX core',
   license="MIT",
   long_description=long_description,
   author='Matthew Scroggs',
   author_email='ceefax@mscroggs.co.uk',
   url="http://www.github.com/mscroggs/CEEFAX",
   packages=['ceefax']
)
