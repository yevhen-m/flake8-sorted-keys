import setuptools

install_requires = [
    "flake8 > 3.0.0",
]

setuptools.setup(
    name="flake8_sorted_keys",
    license="MIT",
    version="0.1.0",
    description="check keys are sorted in dict literals",
    author="yevhen-m, eprykhodko",
    url="https://gitlab.com/yevhen-m/flake8-sorted-keys",
    packages=[
        "flake8_sorted_keys",
    ],
    test_suite='tests',
    install_requires=install_requires,
    entry_points={
        'flake8.extension': [
            'S00 = flake8_sorted_keys:SortedKeysChecker',
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
