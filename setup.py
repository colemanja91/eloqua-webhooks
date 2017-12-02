"""
    API service for Eloqua Webhook support
"""

from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(name='elq-webhook',
      version=__version__,
      description='Eloqua Webhook Integration API',
      author='Jeremiah Coleman',
      author_email='colemanja91@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'pbr',
          'six'
      ]
     )
