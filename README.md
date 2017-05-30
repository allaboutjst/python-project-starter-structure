# pythonstructure

A demo of python repository structure

## Repository Structure

All files

```buildoutcfg
├── LICENSE
├── README.md
├── docs
├── requirements.txt
├── sample
│   ├── __init__.py
│   ├── class_demo.py
│   ├── process
│   │   ├── __init__.py
│   │   └── handler.py
│   ├── str_process.py
│   └── utils
│       ├── __init__.py
│       ├── cleanup.py
│       └── string
│           ├── __init__.py
│           └── case_converter.py
├── setup.py
└── tests
    ├── __init__.py
    ├── package.py
    ├── test_sample.py
    └── test_utils.py
```

## The Actual Module

Actual modules are defined inside ./sample/ folder. 

## License

This is arguably the most important part of your repository, aside from the source code itself. The full license text and copyright claims should exist in this file.

## Setup.py

Package and distribution management. This file should obviously be at the root.

## requirements.txt

Development dependencies.

A Pip requirements file should be placed at the root of the repository. It should specify the dependencies required to contribute to the project: testing, building, and generating documentation.

If your project has no development dependencies, or you prefer development environment setup via setup.py, this file may be unnecessary.

## docs

Package reference documentation.

## tests

Package integration and unit tests. A couple of ways to run tests:

```buildoutcfg
# run all unit tests inside tests folder
py.test tests

# run all unit tests, automatically found by nose
nosetests

# run test suits defined inside setup.py
python setup.py test

# run each individual tests
python python tests/test_utils.py
```

## Makefile

TBD

## scripts

TBD


