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

from __future__ import absolute_import

from pipeline.compilers import CompilerBase
from pipeline.exceptions import CompilerError
from react.jsx import JSXTransformer, TransformError

class JSXCompiler(CompilerBase):
    output_extension = 'js'

    def __init__(self, *args, **kwargs):
        CompilerBase.__init__(self, *args, **kwargs)
        self.transformer = JSXTransformer()

    def match_file(self, path):
        return path.endswith('.jsx')

    def compile_file(self, infile, outfile, outdated=False, force=False):
        if not outdated and not force:
            return
        try:
            return self.transformer.transform(infile, outfile)
        except TransformError as e:
            raise CompilerError(e.message)
