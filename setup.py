from setuptools import setup

setup(
    name='corcondia',
    version='0.1.0',
    author='William Shiao',
    author_email='willshiao@gmail.com',
    packages=['corcondia'],
    scripts=[],
    url='http://pypi.python.org/pypi/corcondia/',
    license='MIT',
    description='An implementation of the CORCONDIA (Core Consistency Diagnostic) in Python.',
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    install_requires=[
        "tensorly",
        "numpy",
    ],
    tests_require=[
        'pytest',
    ],
)