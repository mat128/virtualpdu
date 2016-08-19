# Copyright 2016 Internap
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import subprocess

import sys

import os
from virtualpdu.tests import base


def get_entrypoint_path(entrypoint):
    return os.path.join(os.path.dirname(sys.executable), entrypoint)


class TestEntrypointIntegration(base.TestCase):
    def test_entry_point_returns_hello_world(self):
        self.assertEqual(
            subprocess.check_output([
                sys.executable, get_entrypoint_path('virtualpdu')]),
            b'Hello world\n')
