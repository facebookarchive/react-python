# PyReact

PyReact is a Python wrapper around the [React](http://facebook.github.io/react/) JavaScript library and [JSX](http://facebook.github.io/react/docs/jsx-in-depth.html). 

Specifically, it provides an API to transform JSX files into JavaScript from within your Python application, as well as providing access to the latest React build.


## Installation

**PyPI**: PyReact is hosted on PyPI, and can be installed with `pip`:

    $ pip install PyReact

Alternatively, add it into your `requirements` file:

    PyReact==0.1.0


**Dependencies**: PyReact uses [PyExecJS](https://github.com/doloopwhile/PyExecJS) to execute the bundled React code, which requires that a JS runtime environment is installed on your machine. We don't explicitly set a dependency on a runtime environment; Mac OS X comes bundled with one. If you're on a different platform, we recommend [PyV8](https://code.google.com/p/pyv8/).

## Usage

Transform your JSX files via the provided `jsx` module::

```python    
from react import jsx

# For multiple paths, use the JSXTransformer class.
transformer = jsx.JSXTransformer()
for jsx_path, js_path in my_paths:
    transformer.transform(jsx_path, js_path)

# For a single file, you can use a shortcut method.
jsx.transform('path/to/input/file.jsx', 'path/to/output/file.js')
```

**Django**: PyReact includes a JSX compiler for [django-pipeline](https://github.com/cyberdelia/django-pipeline). Add it to your project's pipeline settings like this:

```python
PIPELINE_COMPILERS = (
  'react.utils.pipeline.JSXCompiler',
)
```


## License

Copyright (c) 2013 Facebook, Inc.
Released under the [Apache License, Version 2.0](LICENSE).