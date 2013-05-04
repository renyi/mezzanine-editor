from setuptools import setup, find_packages

NAME = 'mezzanine-editor'

VERSION = '0.1'

DESCRIPTION = """
Editor workflow for Mezzanine CMS.
"""

setup(
    name=NAME,
    description=DESCRIPTION,
    long_description=open('README.md').read(),
    version=VERSION,
    author='Renyi Khor',
    author_email='renyi.ace@gmail.com',
    url='https://github.com/renyi/mezzanine-editor',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    requires=['mezzanine'],
)
