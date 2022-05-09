from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Numerical General Relativity'
LONG_DESCRIPTION = 'Python package to help numerical calculations in general relativity'

# Setting up
setup(
    name="numgr",
    version=VERSION,
    author="Balázs Pál",
    author_email="pal.balazs@ttk.elte.hu",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # additional packages

    keywords=['numerical', 'general', 'relativity'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ]
)
