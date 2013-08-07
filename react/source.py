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

from os.path import abspath, dirname, isfile, join


JS_ROOT = abspath(join(dirname(__file__), 'js'))

def path_for(react_file):
    path = join(JS_ROOT, react_file)
    if isfile(path):
        return path
    else:
        raise IOError('%s: Could not find specified React file.' % path)
