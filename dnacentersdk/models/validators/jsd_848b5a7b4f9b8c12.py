# -*- coding: utf-8 -*-
"""DNA Center Add a Workflow data model.

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

class JSONSchemaValidator848B5A7B4F9B8C12(object):
    """Add a Workflow request schema definition."""
    def __init__(self):
        super(JSONSchemaValidator848B5A7B4F9B8C12, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'_id': {'type': 'string'}, 'addToInventory': {'type': 'boolean'}, 'addedOn': {'type': 'number'}, 'configId': {'type': 'string'}, 'currTaskIdx': {'type': 'number'}, 'description': {'type': 'string'}, 'endTime': {'type': 'number'}, 'execTime': {'type': 'number'}, 'imageId': {'type': 'string'}, 'instanceType': {'type': 'string', 'enum': ['SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow']}, 'lastupdateOn': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'tasks': {'type': 'array', 'items': {'type': 'object', 'properties': {'currWorkItemIdx': {'type': 'number'}, 'endTime': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'taskSeqNo': {'type': 'number'}, 'timeTaken': {'type': 'number'}, 'type': {'type': 'string'}, 'workItemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'command': {'type': 'string'}, 'endTime': {'type': 'number'}, 'outputStr': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'timeTaken': {'type': 'number'}}}}}}}, 'tenantId': {'type': 'string'}, 'type': {'type': 'string'}, 'useState': {'type': 'string'}, 'version': {'type': 'number'}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False