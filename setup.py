#!/usr/bin/env python3
# step 1: python setup.py sdist bdist_wheel
# step 2: twine upload dist/* --verbose
# https://medium.com/the-research-nest/how-to-publish-your-python-code-as-a-pip-package-in-5-simple-steps-3b36286293ec
"""
Parts of this file were taken from the pyzmq project
(https://github.com/zeromq/pyzmq) which have been permitted for use under the
BSD license. Parts are from lxml (https://github.com/lxml/lxml)
"""
from setuptools import setup

with open('requirements.txt') as requirements_file:
    REQUIRED_MODULES = [line.strip() for line in requirements_file]

with open('requirements-dev.txt') as requirements_dev_file:
    REQUIRED_DEV_MODULES = [line.strip() for line in requirements_dev_file]

def readme():
    with open('README.md') as readme_file:
        return readme_file.read()
    
setup(
    name='stellrent-response',
    author='Marcus R. Magalhães',
    author_email='marcusrodrigues.magalhaes@stellantis.com',
    description='Pattern responses for your API Projects',
    packages=['stellrent_response'],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type='text/markdown',
    install_requires=REQUIRED_MODULES
)