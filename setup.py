from setuptools import setup, find_packages
from react import VERSION


setup(
    name='PyReact',
    version=VERSION,
    author='Kunal Mehta',
    author_email='kunalm@fb.com',
    packages=find_packages(),
    package_data={'js': [
        'js/react.js',
        'js/react.min.js',
        'js/JSXTransformer.js',
    ]},
    url='https://github.com/facebook/PyReact',
    license='Apache-2.0',
    description='Python bridge to JSX & the React JavaScript library.',
    long_description=open('README.rst').read(),
    install_requires=[
        'PyExecJS >= 1.0.4',
    ]
)
