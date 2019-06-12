# -*- coding: utf-8 -*-
"""DNA Center Update Device data model.

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

class JSONSchemaValidator09B0F9Ce4239Ae10(object):
    """Update Device request schema definition."""
    def __init__(self):
        # print("created 09b0-f9ce-4239-ae10")
        super(JSONSchemaValidator09B0F9Ce4239Ae10, self).__init__()
        self._validator = fastjsonschema.compile( {'type': 'object', 'properties': {'_id': {'type': 'string'}, 'deviceInfo': {'type': 'object', 'properties': {'aaaCredentials': {'type': 'object', 'properties': {'password': {'type': 'string'}, 'username': {'type': 'string'}}}, 'addedOn': {'type': 'number'}, 'addnMacAddrs': {'type': 'array', 'items': {'type': 'string'}}, 'agentType': {'type': 'string', 'enum': ['POSIX', 'IOS']}, 'authStatus': {'type': 'string'}, 'authenticatedSudiSerialNo': {'type': 'string'}, 'capabilitiesSupported': {'type': 'array', 'items': {'type': 'string'}}, 'cmState': {'type': 'string', 'enum': ['NotContacted', 'Contacted', 'Disconnected', 'SecuringConnection', 'SecuredConnection', 'Authenticated', 'ErrorSecuringConnection', 'ErrorAuthenticating']}, 'description': {'type': 'string'}, 'deviceSudiSerialNos': {'type': 'array', 'items': {'type': 'string'}}, 'deviceType': {'type': 'string'}, 'featuresSupported': {'type': 'array', 'items': {'type': 'string'}}, 'fileSystemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'freespace': {'type': 'number'}, 'name': {'type': 'string'}, 'readable': {'type': 'boolean'}, 'size': {'type': 'number'}, 'type': {'type': 'string'}, 'writeable': {'type': 'boolean'}}}}, 'firstContact': {'type': 'number'}, 'hostname': {'type': 'string'}, 'httpHeaders': {'type': 'array', 'items': {'type': 'object', 'properties': {'key': {'type': 'string'}, 'value': {'type': 'string'}}}}, 'imageFile': {'type': 'string'}, 'imageVersion': {'type': 'string'}, 'ipInterfaces': {'type': 'array', 'items': {'type': 'object', 'properties': {'ipv4Address': {}, 'ipv6AddressList': {'type': 'array', 'items': {}}, 'macAddress': {'type': 'string'}, 'name': {'type': 'string'}, 'status': {'type': 'string'}}}}, 'lastContact': {'type': 'number'}, 'lastSyncTime': {'type': 'number'}, 'lastUpdateOn': {'type': 'number'}, 'location': {'type': 'object', 'properties': {'address': {'type': 'string'}, 'altitude': {'type': 'string'}, 'latitude': {'type': 'string'}, 'longitude': {'type': 'string'}, 'siteId': {'type': 'string'}}}, 'macAddress': {'type': 'string'}, 'mode': {'type': 'string'}, 'name': {'type': 'string'}, 'neighborLinks': {'type': 'array', 'items': {'type': 'object', 'properties': {'localInterfaceName': {'type': 'string'}, 'localMacAddress': {'type': 'string'}, 'localShortInterfaceName': {'type': 'string'}, 'remoteDeviceName': {'type': 'string'}, 'remoteInterfaceName': {'type': 'string'}, 'remoteMacAddress': {'type': 'string'}, 'remotePlatform': {'type': 'string'}, 'remoteShortInterfaceName': {'type': 'string'}, 'remoteVersion': {'type': 'string'}}}}, 'onbState': {'type': 'string', 'enum': ['NotContacted', 'Connecting', 'ErrorSecuringConnection', 'ErrorAuthenticating', 'Initializing', 'Initialized', 'ErrorInitializing', 'SudiAuthorizing', 'ErrorSudiAuthorizing', 'ExecutingWorkflow', 'ExecutedWorkflow', 'ErrorExecutingWorkflow', 'ExecutingReset', 'ErrorExecutingReset', 'Provisioned']}, 'pid': {'type': 'string'}, 'pnpProfileList': {'type': 'array', 'items': {'type': 'object', 'properties': {'createdBy': {'type': 'string'}, 'discoveryCreated': {'type': 'boolean'}, 'primaryEndpoint': {'type': 'object', 'properties': {'certificate': {'type': 'string'}, 'fqdn': {'type': 'string'}, 'ipv4Address': {}, 'ipv6Address': {}, 'port': {'type': 'number'}, 'protocol': {'type': 'string'}}}, 'profileName': {'type': 'string'}, 'secondaryEndpoint': {'type': 'object', 'properties': {'certificate': {'type': 'string'}, 'fqdn': {'type': 'string'}, 'ipv4Address': {}, 'ipv6Address': {}, 'port': {'type': 'number'}, 'protocol': {'type': 'string'}}}}}}, 'populateInventory': {'type': 'boolean'}, 'preWorkflowCliOuputs': {'type': 'array', 'items': {'type': 'object', 'properties': {'cli': {'type': 'string'}, 'cliOutput': {'type': 'string'}}}}, 'projectId': {'type': 'string'}, 'projectName': {'type': 'string'}, 'reloadRequested': {'type': 'boolean'}, 'serialNumber': {'type': 'string'}, 'smartAccountId': {'type': 'string'}, 'source': {'type': 'string'}, 'stack': {'type': 'boolean'}, 'stackInfo': {'type': 'object', 'properties': {'isFullRing': {'type': 'boolean'}, 'stackMemberList': {'type': 'array', 'items': {'type': 'object', 'properties': {'hardwareVersion': {'type': 'string'}, 'licenseLevel': {'type': 'string'}, 'licenseType': {'type': 'string'}, 'macAddress': {'type': 'string'}, 'pid': {'type': 'string'}, 'priority': {'type': 'number'}, 'role': {'type': 'string'}, 'serialNumber': {'type': 'string'}, 'softwareVersion': {'type': 'string'}, 'stackNumber': {'type': 'number'}, 'state': {'type': 'string'}, 'sudiSerialNumber': {'type': 'string'}}}}, 'stackRingProtocol': {'type': 'string'}, 'supportsStackWorkflows': {'type': 'boolean'}, 'totalMemberCount': {'type': 'number'}, 'validLicenseLevels': {'type': 'array', 'items': {'type': 'string'}}}}, 'state': {'type': 'string', 'enum': ['Unclaimed', 'Planned', 'Onboarding', 'Provisioned', 'Error', 'Deleted']}, 'sudiRequired': {'type': 'boolean'}, 'tags': {}, 'userSudiSerialNos': {'type': 'array', 'items': {'type': 'string'}}, 'virtualAccountId': {'type': 'string'}, 'workflowId': {'type': 'string'}, 'workflowName': {'type': 'string'}}}, 'runSummaryList': {'type': 'array', 'items': {'type': 'object', 'properties': {'details': {'type': 'string'}, 'errorFlag': {'type': 'boolean'}, 'historyTaskInfo': {'type': 'object', 'properties': {'addnDetails': {'type': 'array', 'items': {'type': 'object', 'properties': {'key': {'type': 'string'}, 'value': {'type': 'string'}}}}, 'name': {'type': 'string'}, 'timeTaken': {'type': 'number'}, 'type': {'type': 'string'}, 'workItemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'command': {'type': 'string'}, 'endTime': {'type': 'number'}, 'outputStr': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'timeTaken': {'type': 'number'}}}}}}, 'timestamp': {'type': 'number'}}}}, 'systemResetWorkflow': {'type': 'object', 'properties': {'_id': {'type': 'string'}, 'addToInventory': {'type': 'boolean'}, 'addedOn': {'type': 'number'}, 'configId': {'type': 'string'}, 'currTaskIdx': {'type': 'number'}, 'description': {'type': 'string'}, 'endTime': {'type': 'number'}, 'execTime': {'type': 'number'}, 'imageId': {'type': 'string'}, 'instanceType': {'type': 'string', 'enum': ['SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow']}, 'lastupdateOn': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'tasks': {'type': 'array', 'items': {'type': 'object', 'properties': {'currWorkItemIdx': {'type': 'number'}, 'endTime': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'taskSeqNo': {'type': 'number'}, 'timeTaken': {'type': 'number'}, 'type': {'type': 'string'}, 'workItemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'command': {'type': 'string'}, 'endTime': {'type': 'number'}, 'outputStr': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'timeTaken': {'type': 'number'}}}}}}}, 'tenantId': {'type': 'string'}, 'type': {'type': 'string'}, 'useState': {'type': 'string'}, 'version': {'type': 'number'}}}, 'systemWorkflow': {'type': 'object', 'properties': {'_id': {'type': 'string'}, 'addToInventory': {'type': 'boolean'}, 'addedOn': {'type': 'number'}, 'configId': {'type': 'string'}, 'currTaskIdx': {'type': 'number'}, 'description': {'type': 'string'}, 'endTime': {'type': 'number'}, 'execTime': {'type': 'number'}, 'imageId': {'type': 'string'}, 'instanceType': {'type': 'string', 'enum': ['SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow']}, 'lastupdateOn': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'tasks': {'type': 'array', 'items': {'type': 'object', 'properties': {'currWorkItemIdx': {'type': 'number'}, 'endTime': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'taskSeqNo': {'type': 'number'}, 'timeTaken': {'type': 'number'}, 'type': {'type': 'string'}, 'workItemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'command': {'type': 'string'}, 'endTime': {'type': 'number'}, 'outputStr': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'timeTaken': {'type': 'number'}}}}}}}, 'tenantId': {'type': 'string'}, 'type': {'type': 'string'}, 'useState': {'type': 'string'}, 'version': {'type': 'number'}}}, 'tenantId': {'type': 'string'}, 'version': {'type': 'number'}, 'workflow': {'type': 'object', 'properties': {'_id': {'type': 'string'}, 'addToInventory': {'type': 'boolean'}, 'addedOn': {'type': 'number'}, 'configId': {'type': 'string'}, 'currTaskIdx': {'type': 'number'}, 'description': {'type': 'string'}, 'endTime': {'type': 'number'}, 'execTime': {'type': 'number'}, 'imageId': {'type': 'string'}, 'instanceType': {'type': 'string', 'enum': ['SystemWorkflow', 'UserWorkflow', 'SystemResetWorkflow']}, 'lastupdateOn': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'tasks': {'type': 'array', 'items': {'type': 'object', 'properties': {'currWorkItemIdx': {'type': 'number'}, 'endTime': {'type': 'number'}, 'name': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'taskSeqNo': {'type': 'number'}, 'timeTaken': {'type': 'number'}, 'type': {'type': 'string'}, 'workItemList': {'type': 'array', 'items': {'type': 'object', 'properties': {'command': {'type': 'string'}, 'endTime': {'type': 'number'}, 'outputStr': {'type': 'string'}, 'startTime': {'type': 'number'}, 'state': {'type': 'string'}, 'timeTaken': {'type': 'number'}}}}}}}, 'tenantId': {'type': 'string'}, 'type': {'type': 'string'}, 'useState': {'type': 'string'}, 'version': {'type': 'number'}}}, 'workflowParameters': {'type': 'object', 'properties': {'configList': {'type': 'array', 'items': {'type': 'object', 'properties': {'configId': {'type': 'string'}, 'configParameters': {'type': 'array', 'items': {'type': 'object', 'properties': {'key': {'type': 'string'}, 'value': {'type': 'string'}}}}}}}, 'licenseLevel': {'type': 'string'}, 'licenseType': {'type': 'string'}, 'topOfStackSerialNumber': {'type': 'string'}}}}} )

    def validate(self, request):
        try:
            self._validator(request)
            return True
        except fastjsonschema.exceptions.JsonSchemaException as e:
            raise MalformedRequest('{} is invalid. Reason: {}'.format(request, e.message))
            return False