### NOTE: This project is no longer actively maintained.

# PyReact

PyReact is a Python wrapper around the [React](http://facebook.github.io/react/) JavaScript library and [JSX](http://facebook.github.io/react/docs/jsx-in-depth.html).

Specifically, it provides an API to transform JSX files into JavaScript from within your Python application, as well as providing access to the latest React build.


## Installation

**PyPI**: PyReact is hosted on PyPI, and can be installed with `pip`:

    $ pip install PyReact

Alternatively, add it into your `requirements` file:

    PyReact==0.6.0


**Dependencies**: PyReact uses [PyExecJS](https://github.com/doloopwhile/PyExecJS) to execute the bundled React code, which requires that a JS runtime environment is installed on your machine. We don't explicitly set a dependency on a runtime environment; Mac OS X comes bundled with one. If you're on a different platform, we recommend [PyV8](https://code.google.com/p/pyv8/).

## Usage

Transform your JSX files via the provided `jsx` module::

```python
from react import jsx

# For multiple paths, use the JSXTransformer class.
transformer = jsx.JSXTransformer()
for jsx_path, js_path in my_paths:
    transformer.transform(jsx_path, js_path=js_path)

# For a single file, you can use a shortcut method.
jsx.transform('path/to/input/file.jsx', js_path='path/to/output/file.js')
```

You can also use ``transform_string(jsx)`` method to transform strings:

```python
from react import jsx
transformer = jsx.JSXTransformer()
js = transformer.transform_string(jsx)
```

**Django**: PyReact includes a JSX compiler for [django-pipeline](https://github.com/cyberdelia/django-pipeline). It has been tested with django-pipeline 1.3.20, but may work with other versions too. Add it to your project's pipeline settings like this:

```python
PIPELINE_COMPILERS = (
  'react.utils.pipeline.JSXCompiler',
)
```


## License

Copyright (c) 2013 Facebook, Inc.
Released under the [Apache License, Version 2.0](LICENSE).
