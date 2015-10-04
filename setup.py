try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

from setuptools.command.test import test as test_command
import sys


class PyTest(test_command):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        test_command.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        test_command.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='pyproject',
    version='0.1',
    description='',
    packages=find_packages(exclude=['tests']),
    namespace_packages=['pyproject'],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
    ],
    setup_requires=[
        'argparse',
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    entry_points={
        'console_scripts': [
        ]
    },
)
