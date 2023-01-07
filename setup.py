from setuptools import find_packages, setup

setup(
    name="flitton_fib_py",
    version="0.0.1",
    author="Zou Bibo",
    author_email="zoubibo@amiunique.net",
    description="Calculates a Fibonacci number",
    long_description="A basic library that \
      calculates Fibonacci numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/hekinami/flitton- \
      fib-py",

    install_requires=[],

    packages=find_packages(exclude=("tests",)),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)
