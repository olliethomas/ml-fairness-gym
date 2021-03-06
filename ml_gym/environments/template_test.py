# coding=utf-8
# Copyright 2020 The ML Fairness Gym Authors.
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

"""Tests for fairness_gym.environments.template."""

from __future__ import absolute_import, division, print_function

from absl.testing import absltest

import test_util
from ml_gym.environments import template


class TemplateTest(absltest.TestCase):
    def test_example_environment_can_run(self):
        test_util.run_test_simulation(env=template.ExampleEnv())


if __name__ == "__main__":
    absltest.main()
