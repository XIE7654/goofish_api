from setuptools import setup
from goofish_api.__version__ import __version__

setup(
    name='goofish_api',
    version=__version__,
    install_requires=[
    ],
    packages=[
        'goofish_api',
        'goofish_api.api',
        'goofish_api.utils',
    ],
    url='https://github.com/xie7654/goofish_api',
    license='MIT',
    author='XIE JUN',
    author_email='xie765462425@gmail.com',
    description='Python wrapper for the goofish API',
)