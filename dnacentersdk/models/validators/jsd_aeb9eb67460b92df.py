# -*- coding: utf-8 -*-
"""DNA Center Sync Devices data model.

Copyright (c) 2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import fastjsonschema
from dnacentersdk.exceptions import MalformedRequest

from builtins import *

class JSONSchemaValidatorAeb9Eb67460B92Df(object):
    """Sync Devices request schema definition."""
    def __init__(self):
        # print("created aeb9-eb67-460b-92df")
        super(JSONSchemaValidatorAeb9Eb67460B92Df, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'cliTransport': {'type': 'string'}, 'computeDevice': {'type': 'boolean'}, 'enablePassword': {'type': 'string'}, 'extendedDiscoveryInfo': {'type': 'string'}, 'httpPassword': {'type': 'string'}, 'httpPort': {'type': 'string'}, 'httpSecure': {'type': 'boolean'}, 'httpUserName': {'type': 'string'}, 'ipAddress': {'type': 'array', 'items': {'type': 'string'}}, 'merakiOrgId': {'type': 'array', 'items': {'type': 'string'}}, 'netconfPort': {'type': 'string'}, 'password': {'type': 'string'}, 'serialNumber': {'type': 'string'}, 'snmpAuthPassphrase': {'type': 'string'}, 'snmpAuthProtocol': {'type': 'string'}, 'snmpMode': {'type': 'string'}, 'snmpPrivPassphrase': {'type': 'string'}, 'snmpPrivProtocol': {'type': 'string'}, 'snmpROCommunity': {'type': 'string'}, 'snmpRWCommunity': {'type': 'string'}, 'snmpRetry': {'type': 'number'}, 'snmpTimeout': {'type': 'number'}, 'snmpUserName': {'type': 'string'}, 'snmpVersion': {'type': 'string'}, 'type': {'type': 'string', 'enum': ['COMPUTE_DEVICE', 'MERAKI_DASHBOARD', 'NETWORK_DEVICE', 'NODATACHANGE']}, 'updateMgmtIPaddressList': {'type': 'array', 'items': {'type': 'object', 'properties': {'existMgmtIpAddress': {'type': 'string'}, 'newMgmtIpAddress': {'type': 'string'}}}}, 'userName': {'type': 'string'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False