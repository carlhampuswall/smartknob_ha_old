from setuptools import setup, find_packages

setup(
    name="smartknobpylib",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
    ],
    entry_points={
        "console_scripts": [
            "tests = smartknobpylib.tests:run_tests",
        ],
    },
)
