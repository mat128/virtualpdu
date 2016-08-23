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

from mock import mock
from virtualpdu import core
from virtualpdu import drivers
from virtualpdu import power_states
from virtualpdu.tests import base


class TestCore(base.TestCase):
    def setUp(self):
        super(TestCore, self).setUp()
        self.driver_mock = mock.create_autospec(drivers.Driver)

    def test_pdu_outlet_state_changed_power_off(self):
        mapping = {
            ('my_pdu', 1): 'server_one'
        }

        self.core = core.Core(driver=self.driver_mock, mapping=mapping)

        self.core.pdu_outlet_state_changed(name='my_pdu',
                                           outlet_number=1,
                                           state=power_states.POWER_OFF)

        self.driver_mock.power_off.assert_called_with('server_one')

    def test_pdu_outlet_state_changed_machine_not_in_mapping_noop(self):
        mapping = {
            ('my_pdu', 1): 'server_one'
        }

        self.core = core.Core(driver=self.driver_mock, mapping=mapping)

        self.core.pdu_outlet_state_changed(name='my_pdu',
                                           outlet_number=2,
                                           state=power_states.POWER_OFF)

        self.assertFalse(self.driver_mock.power_off.called)
        self.assertFalse(self.driver_mock.power_on.called)

    def test_pdu_outlet_state_changed_power_on(self):
        mapping = {
            ('my_pdu', 1): 'server_one'
        }

        self.core = core.Core(driver=self.driver_mock, mapping=mapping)

        self.core.pdu_outlet_state_changed(name='my_pdu',
                                           outlet_number=1,
                                           state=power_states.POWER_ON)

        self.driver_mock.power_on.assert_called_with('server_one')

    def test_pdu_outlet_state_changed_reboot(self):
        mapping = {
            ('my_pdu', 1): 'server_one'
        }

        self.core = core.Core(driver=self.driver_mock, mapping=mapping)

        self.core.pdu_outlet_state_changed(name='my_pdu',
                                           outlet_number=1,
                                           state=power_states.REBOOT)

        self.driver_mock.assert_has_calls([mock.call.power_off('server_one'),
                                           mock.call.power_on('server_one')])
