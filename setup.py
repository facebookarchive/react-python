from setuptools import setup, find_packages
from react import VERSION


setup(
    name='PyReact',
    version=VERSION,
    author='Kunal Mehta',
    author_email='kunalm@fb.com',
    url='https://github.com/reactjs/react-python/',
    license='Apache-2.0',
    description='Python bridge to JSX & the React JavaScript library.',
    long_description=open('DESCRIPTION').read(),
    classifiers =[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages(),
    include_package_data=True,
    package_data={'js': [
        'js/react/react.js',
        'js/react/react.min.js',
        'js/react/react-with-addons.js',
        'js/react/react-with-addons.min.js',
        'js/react/JSXTransformer.js',
    ]},
    install_requires=[
        'PyExecJS >= 1.0.4',
    ]
)
