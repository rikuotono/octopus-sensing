# This file is part of Octopus Sensing <https://octopus-sensing.nastaran-saffar.me/>
# Copyright © Nastaran Saffaryazdi 2020
#
# Octopus Sensing is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software Foundation,
#  either version 3 of the License, or (at your option) any later version.
#
# Octopus Sensing is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Octopus Sensing.
# If not, see <https://www.gnu.org/licenses/>.

from octopus_sensing.common.endpoint_base import EndpointBase


class MonitoringEndpoint(EndpointBase):

    def __init__(self, device_coordinator):
        super().__init__(endpoint_name="MonitoringEndpoint-Thread",
                         port=9330, get_callback=self._get_handler)
        self._device_coordinator = device_coordinator

    def _get_handler(self, request_reader):
        return self._device_coordinator.get_monitoring_data()
