# Copyright 2013 Facebook, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import execjs
import react.source


class JSXTransformer(object):

    JSX_TRANSFORMER_JS_EXPR = '(global.JSXTransformer || module.exports)'

    def __init__(self):
        path = react.source.path_for('JSXTransformer.js')
        with open(path, 'rU') as f:
            self.context = execjs.compile(f.read())

    def transform_string(self, jsx, harmony=False, strip_types=False):
        """ Transform ``jsx`` JSX string into javascript

        :param jsx: JSX source code
        :type jsx: basestring
        :keyword harmony: Transform ES6 code into ES3 (default: False)
        :type harmony: bool
        :keyword strip_types: Strip type declarations (default: False)
        :type harmony: bool
        :return: compiled JS code
        :rtype: str
        """
        opts = {'harmony': harmony, 'stripTypes': strip_types}
        try:
            result = self.context.call(
                '%s.transform' % self.JSX_TRANSFORMER_JS_EXPR, jsx, opts)
        except execjs.ProgramError as e:
            raise TransformError(str(e))
        js = result['code']
        return js

    def transform(self, jsx_path, js_path=None, **kwargs):
        with open(jsx_path, 'rU') as i:
            js = self.transform_string(i.read(), **kwargs)
            if js_path:
                with open(js_path, 'wb') as o:
                    o.write(js.encode('utf8'))
            return js


class TransformError(Exception):
    def __init__(self, message):
        Exception.__init__(self, message)


def transform(jsx_path, **opts):
    return JSXTransformer().transform(jsx_path, **opts)

def transform_string(jsx, **opts):
    return JSXTransformer().transform_string(jsx, **opts)
