import os
from setuptools import setup, find_packages


def read(*paths):
    """Read the contents of a text file safely
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    """
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath, *paths)
    with open(filepath) as file_:
        return file_.read().strip()


def read_requirements(path):
    """Return a list of requirements from a text file"""
    return [
        line.strip()
        for line in read(path).split('\n') if not line.startswith(
            ('#', 'git+', '"', '-')
        )
    ]


setup(
    name='dundie',
    version='0.1.0',
    description='Reward Point System for Dunder Mifflin',
    author="Robson Santos",
    packages=find_packages(),
    entry_points={
        'console_scripts': ['dundie = dundie.__main__:main']
    },
    install_requires=read_requirements('requirements.txt'),
    extras_require = { # noqa
        'test': read_requirements('requirements.test.txt'),
        'dev': read_requirements('requirements.dev.txt')
    }
)
