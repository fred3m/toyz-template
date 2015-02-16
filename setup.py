
import os
import sys
import glob
from toyz import version
from setuptools import setup
from setuptools import find_packages

# Package info
PACKAGE_NAME = "toyz_template" # change this to the name of your new toyz module
DESCRIPTION = "Template for new Toyz" # Short description of your module
LONG_DESC = "For this repository to create your own toyz" # Longer Description of your module
AUTHOR = "myname" # Your name here
AUTHOR_EMAIL = "myemail@host.com" # your email here
LICENSE = "MIT" # or whatever licese you wish to use
URL = "www.your_webpage_here.com" # your webpage here

# VERSION should be PEP386 compatible (http://www.python.org/dev/peps/pep-0386)
VERSION = '0.0.dev'

if 'dev' not in VERSION:
    VERSION += version.get_git_devstr(False)

scripts = [fname for fname in glob.glob(os.path.join('scripts', '*'))
           if os.path.basename(fname) != 'README.rst']

packages = find_packages()

setup(name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    packages=packages,
    scripts=scripts,
    requires=[
        'tornado',
        'toyz'
    ],
    #install_requires=[],
    #provides=[PACKAGE_NAME],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    url=URL,
    long_description=LONG_DESC,
    zip_safe=False,
    use_2to3=True,
    include_package_data=True
)