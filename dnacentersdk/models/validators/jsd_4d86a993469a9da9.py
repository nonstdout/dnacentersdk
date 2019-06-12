# -*- coding: utf-8 -*-
"""DNA Center Update Tag data model.

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

class JSONSchemaValidator4D86A993469A9Da9(object):
    """Update Tag request schema definition."""
    def __init__(self):
        # print("created 4d86-a993-469a-9da9")
        super(JSONSchemaValidator4D86A993469A9Da9, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'systemTag': {'type': 'boolean'}, 'description': {'type': 'string'}, 'dynamicRules': {'type': 'array', 'items': {'type': 'object', 'properties': {'memberType': {'type': 'string'}, 'rules': {'type': 'object', 'properties': {'values': {'type': 'array', 'items': {'type': 'string'}}, 'items': {'type': 'array', 'items': {'type': 'string'}}, 'operation': {'type': 'string'}, 'name': {'type': 'string'}, 'value': {'type': 'string'}}}}}}, 'name': {'type': 'string'}, 'id': {'type': 'string'}, 'instanceTenantId': {'type': 'string'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False