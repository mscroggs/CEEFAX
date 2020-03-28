import os
from setuptools import setup

os.system("cp VERSION LICENSE.txt contributors.txt ceefax/")

with open("README.md") as f:
    long_description = f.read()

with open("VERSION") as f:
    v = f.read()

setup(
   name='ceefax',
   version=v,
   description='CEEFAX core',
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   author='Matthew Scroggs',
   author_email='ceefax@mscroggs.co.uk',
   url="http://www.github.com/mscroggs/CEEFAX",
   packages=['ceefax', 'ceefax.ceefax', 'ceefax.ceegraph', 'ceefax.cupt',
             'ceefax.error', 'ceefax.fonts', 'ceefax.functions', 'ceefax.helpers',
             'ceefax.page', 'ceefax.pages',
             'ceefax.fonts.size3', 'ceefax.fonts.size4bold', 'ceefax.fonts.size7',
             'ceefax.fonts.size7extracondensed', 'ceefax.fonts.size4',
             'ceefax.fonts.size4mono', 'ceefax.fonts.size7condensed'],
   package_data={'': ['VERSION', 'LICENSE.txt', 'contributors.txt']},
   include_package_data=True,
)
