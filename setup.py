from setuptools import setup
from _install_hook import _InstallCommand

setup(cmdclass={'install': _InstallCommand})
