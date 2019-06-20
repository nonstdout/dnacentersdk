# -*- coding: utf-8 -*-
"""DNA Center API wrappers.

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

from past.types import basestring

from dnacentersdk.config import (
    DEFAULT_BASE_URL, DEFAULT_SINGLE_REQUEST_TIMEOUT,
    DEFAULT_WAIT_ON_RATE_LIMIT, DEFAULT_VERIFY,
)
from dnacentersdk.environment import DNA_CENTER_ACCESS_TOKEN
from dnacentersdk.exceptions import AccessTokenError
from dnacentersdk.models.mydict import mydict_data_factory
from dnacentersdk.models.schema_validator import json_schema_validate
from dnacentersdk.restsession import RestSession
from dnacentersdk.utils import check_type

from .authentication import Authentication
from .templateprogrammer import TemplateProgrammer
from .tag import Tag
from .networkdiscovery import NetworkDiscovery
from .task import Task
from .commandrunner import CommandRunner
from .file import File
from .pathtrace import PathTrace
from .swim import Swim
from .pnp import Pnp
from .siteprofile import SiteProfile
from .devices import Devices
from .sites import Sites
from .networks import Networks
from .clients import Clients
from .nonfabricwireless import NonFabricWireless
from .fabricwired import FabricWired



class DNACenterAPI(object):
    """DNA Center API wrapper.

    Creates a 'session' for all API calls through a created DNACenterAPI
    object.  The 'session' handles authentication, provides the needed headers,
    and checks all responses for error conditions.

    DNACenterAPI wraps all of the individual DNA Center APIs and represents
    them in a simple hierarchical structure.
    """

    def __init__(self, access_token=None, base_url=DEFAULT_BASE_URL,
                 single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT,
                 wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT,
                 verify=DEFAULT_VERIFY,
                 object_factory=mydict_data_factory,
                 request_validator=json_schema_validate,
                 username=None,
                 password=None,
                 encodedAuth=None):
        """Create a new DNACenterAPI object.

        An access token must be used when interacting with the DNA Center API.
        This package supports three methods for you to provide that access
        token:

        . . .

        An AccessTokenError is raised if an access token is not provided
        via one of these two methods.

        Args:
            access_token(basestring): The access token to be used for API
                calls to the DNA Center service.  Defaults to checking for a
                DNA_CENTER_ACCESS_TOKEN environment variable.
            base_url(basestring): The base URL to be prefixed to the
                individual API endpoint suffixes.
                Defaults to dnacentersdk.DEFAULT_BASE_URL.
            single_request_timeout(int): Timeout (in seconds) for RESTful HTTP
                requests. Defaults to
                dnacentersdk.config.DEFAULT_SINGLE_REQUEST_TIMEOUT.
            wait_on_rate_limit(bool): Enables or disables automatic rate-limit
                handling. Defaults to
                dnacentersdk.config.DEFAULT_WAIT_ON_RATE_LIMIT.
            verify(bool,basestring): Controls whether we verify the server’s TLS certificate, or a string, in which case it must be a path to a CA bundle to use. Defaults to 
                dnacentersdk.config.DEFAULT_VERIFY.
            object_factory(callable): The factory function to use to create
                Python objects from the returned DNA Center JSON data objects.

        Returns:
            DNACenterAPI: A new DNACenterAPI object.

        Raises:
            TypeError: If the parameter types are incorrect.
            AccessTokenError: If an access token is not provided via the
                access_token argument or an environment variable.

        """
        check_type(access_token, basestring, may_be_none=True)
        check_type(base_url, basestring)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool)
        check_type(username, basestring, may_be_none=True)
        check_type(password, basestring, may_be_none=True)
        check_type(encodedAuth, basestring, may_be_none=True)
        check_type(verify, (bool, basestring), may_be_none=False)

        access_token = access_token or DNA_CENTER_ACCESS_TOKEN

        # Init AccessTokensAPI wrapper early to use for oauth requests
        self.authentication = Authentication(
            base_url, object_factory,
            single_request_timeout=single_request_timeout,
            verify=verify,
        )

        # Check if the user has provided the required basicAuth parameters
        has_basic_auth = all([username, password]) or all([encodedAuth])
        if not access_token and has_basic_auth:
            access_token = self.authentication.authentication_api(
                username=username,
                password=password,
                encodedAuth=encodedAuth
            ).Token
        
        # If an access token hasn't been provided as a parameter, environment
        # variable, or obtained via an OAuth exchange raise an error.
        if not access_token:
            raise AccessTokenError(
                "You must provide a DNA Center access token to interact with "
                "the DNA Center APIs, either via a DNA_CENTER_ACCESS_TOKEN "
                "environment variable or via the access_token argument."
                "To interact with the APIs and get your access_token, you could provide" 
                "either username and password arguments or via the encodedAuth argument."
            )

        # Create the API session
        # All of the API calls associated with a DNACenterAPI object will
        # leverage a single RESTful 'session' connecting to the DNA Center
        # cloud.
        self._session = RestSession(
            access_token=access_token,
            base_url=base_url,
            single_request_timeout=single_request_timeout,
            wait_on_rate_limit=wait_on_rate_limit,
            verify=verify,
        )

        # API wrappers
        self.template_programmer = TemplateProgrammer(self._session, object_factory, request_validator)
        self.tag = Tag(self._session, object_factory, request_validator)
        self.network_discovery = NetworkDiscovery(self._session, object_factory, request_validator)
        self.task = Task(self._session, object_factory, request_validator)
        self.command_runner = CommandRunner(self._session, object_factory, request_validator)
        self.file = File(self._session, object_factory, request_validator)
        self.path_trace = PathTrace(self._session, object_factory, request_validator)
        self.swim = Swim(self._session, object_factory, request_validator)
        self.pnp = Pnp(self._session, object_factory, request_validator)
        self.site_profile = SiteProfile(self._session, object_factory, request_validator)
        self.devices = Devices(self._session, object_factory, request_validator)
        self.sites = Sites(self._session, object_factory, request_validator)
        self.networks = Networks(self._session, object_factory, request_validator)
        self.clients = Clients(self._session, object_factory, request_validator)
        self.non_fabric_wireless = NonFabricWireless(self._session, object_factory, request_validator)
        self.fabric_wired = FabricWired(self._session, object_factory, request_validator)

    @property
    def access_token(self):
        """The access token used for API calls to the DNA Center service."""
        return self._session.access_token

    @property
    def base_url(self):
        """The base URL prefixed to the individual API endpoint suffixes."""
        return self._session.base_url

    @property
    def single_request_timeout(self):
        """Timeout (in seconds) for an single HTTP request."""
        return self._session.single_request_timeout

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling enabled / disabled."""
        return self._session.wait_on_rate_limit

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._session._verify