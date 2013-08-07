PyReact
=======

PyReact is a Python wrapper around the `React <http://facebook.github.io/react/>`_ JavaScript library and `JSX <http://facebook.github.io/react/docs/jsx-in-depth.html>`_. 

Specifically, it provides an API to transform JSX files into JavaScript from within your Python application, as well as providing access to the latest React build.


Installation
------------

PyReact is hosted on PyPI, and can be installed with ``pip``::

    $ pip install PyReact

Alternatively, add it into your ``requirements`` file::

    PyReact==0.1.0


Usage
-----

Transform your JSX files via the provided ``jsx`` module::
    
    from react import jsx

    # For multiple paths, use the JSXTransformer class.
    transformer = jsx.JSXTransformer()
    for input, output in my_paths:
        transformer.transform(input, output)

    # For a single file, you can use a shortcut method.
    jsx.transform('path/to/input/file.jsx', 'path/to/output/file.js')


License
-------

Copyright (c) 2013 Facebook, Inc.
Released under the Apache License, Version 2.0.