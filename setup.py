from setuptools import setup, find_packages
from hotel import __version__

setup(
    name='hotel',
    version=__version__,

    url='http://host/',
    author='author',
    author_email='email',

    packages=find_packages(),
    include_package_data=True,
    scripts=['scripts/manage.py'],

    #install_requires=(
    #    'django<1.7',
    #)
)
