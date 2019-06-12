# -*- coding: utf-8 -*-
"""DNA Center Create Enterprise SSID data model.

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

class JSONSchemaValidator8A96Fb954D09A349(object):
    """Create Enterprise SSID request schema definition."""
    def __init__(self):
        # print("created 8a96-fb95-4d09-a349")
        super(JSONSchemaValidator8A96Fb954D09A349, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'name': {'type': 'string', 'maxLength': 32}, 'securityLevel': {'type': 'string', 'enum': ['WPA2_ENTERPRISE', 'WPA2_PERSONAL', 'OPEN']}, 'passphrase': {'type': 'string', 'maxLength': 63, 'minLength': 8}, 'enableFastLane': {'type': 'boolean'}, 'enableMACFiltering': {'type': 'boolean'}, 'trafficType': {'type': 'string', 'enum': ['voicedata', 'data']}, 'radioPolicy': {'type': 'string', 'enum': ['Dual band operation (2.4GHz and 5GHz)', 'Dual band operation with band select', '5GHz only', '2.4GHz only']}, 'enableBroadcastSSID': {'type': 'boolean'}, 'fastTransition': {'type': 'string', 'enum': ['Adaptive', 'Enable', 'Disable']}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False