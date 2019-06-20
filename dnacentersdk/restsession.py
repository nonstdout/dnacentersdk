# -*- coding: utf-8 -*-
"""RestSession class for creating connections to the DNA Center APIs.

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

from future import standard_library
standard_library.install_aliases()

import time
import urllib.parse
import warnings
from builtins import *

import requests
from past.builtins import basestring

from .config import DEFAULT_SINGLE_REQUEST_TIMEOUT, DEFAULT_WAIT_ON_RATE_LIMIT, DEFAULT_VERIFY
from .exceptions import MalformedResponse, RateLimitError, RateLimitWarning, DownloadFailure
from .response_codes import EXPECTED_RESPONSE_CODE
from .utils import (
    check_response_code, check_type, extract_and_parse_json, validate_base_url,
)


# Main module interface
class RestSession(object):
    """RESTful HTTP session class for making calls to the DNA Center APIs."""

    def __init__(self, access_token, base_url
        , single_request_timeout=DEFAULT_SINGLE_REQUEST_TIMEOUT
        , wait_on_rate_limit=DEFAULT_WAIT_ON_RATE_LIMIT 
        , verify = DEFAULT_VERIFY):
        """Initialize a new RestSession object.

        Args:
            access_token(basestring): The DNA Center access token to be used
                for this session.
            base_url(basestring): The base URL that will be suffixed onto API
                endpoint relative URLs to produce a callable absolute URL.
            single_request_timeout(int): The timeout (seconds) for a single
                HTTP REST API request.
            wait_on_rate_limit(bool): Enable or disable automatic rate-limit
                handling.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(access_token, basestring, may_be_none=False)
        check_type(base_url, basestring, may_be_none=False)
        check_type(single_request_timeout, int)
        check_type(wait_on_rate_limit, bool, may_be_none=False)
        check_type(verify, (bool, basestring), may_be_none=False)


        super(RestSession, self).__init__()

        # Initialize attributes and properties
        self._base_url = str(validate_base_url(base_url))
        self._access_token = str(access_token)
        self._single_request_timeout = single_request_timeout
        self._wait_on_rate_limit = wait_on_rate_limit
        self._verify = verify

        # Initialize a new `requests` session
        self._req_session = requests.session()

        # Update the headers of the `requests` session
        self.update_headers({'X-Auth-Token': access_token,
                             'Content-type': 'application/json;charset=utf-8'})

    @property
    def verify(self):
        """The verify (TLS Certificate) for the API endpoints."""
        return self._verify

    @verify.setter
    def verify(self, value):
        """Enable or disable automatic rate-limit handling."""
        check_type(value, bool, may_be_none=False)
        self._verify = value

    @property
    def base_url(self):
        """The base URL for the API endpoints."""
        return self._base_url

    @property
    def access_token(self):
        """The DNA Center access token used for this session."""
        return self._access_token

    @property
    def single_request_timeout(self):
        """The timeout (seconds) for a single HTTP REST API request."""
        return self._single_request_timeout

    @single_request_timeout.setter
    def single_request_timeout(self, value):
        """The timeout (seconds) for a single HTTP REST API request."""
        check_type(value, int)
        assert value is None or value > 0
        self._single_request_timeout = value

    @property
    def wait_on_rate_limit(self):
        """Automatic rate-limit handling.

        This setting enables or disables automatic rate-limit handling.  When
        enabled, rate-limited requests will be automatically be retried after
        waiting `Retry-After` seconds (provided by DNA Center in the
        rate-limit response header).

        """
        return self._wait_on_rate_limit

    @wait_on_rate_limit.setter
    def wait_on_rate_limit(self, value):
        """Enable or disable automatic rate-limit handling."""
        check_type(value, bool, may_be_none=False)
        self._wait_on_rate_limit = value

    @property
    def headers(self):
        """The HTTP headers used for requests in this session."""
        return self._req_session.headers.copy()

    def update_headers(self, headers):
        """Update the HTTP headers used for requests in this session.

        Note: Updates provided by the dictionary passed as the `headers`
        parameter to this method are merged into the session headers by adding
        new key-value pairs and/or updating the values of existing keys. The
        session headers are not replaced by the provided dictionary.

        Args:
             headers(dict): Updates to the current session headers.

        """
        check_type(headers, dict, may_be_none=False)
        self._req_session.headers.update(headers)

    def abs_url(self, url):
        """Given a relative or absolute URL; return an absolute URL.

        Args:
            url(basestring): A relative or absolute URL.

        Returns:
            str: An absolute URL.

        """
        parsed_url = urllib.parse.urlparse(url)
        if not parsed_url.scheme and not parsed_url.netloc:
            # url is a relative URL; combine with base_url
            return urllib.parse.urljoin(str(self.base_url), str(url))
        else:
            # url is already an absolute URL; return as is
            return url

    def get_filename_from_cd(self, cd):
        """
        Get filename from content-disposition
        """
        if not cd:
            return None
        fname = re.findall('filename=(.+)', cd)
        if len(fname) == 0:
            return None
        return fname[0]


    def request(self, method, url, erc, **kwargs):
        """Abstract base method for making requests to the DNA Center APIs.

        This base method:
            * Expands the API endpoint URL to an absolute URL
            * Makes the actual HTTP request to the API endpoint
            * Provides support for DNA Center rate-limiting
            * Inspects response codes and raises exceptions as appropriate

        Args:
            method(basestring): The request-method type ('GET', 'POST', etc.).
            url(basestring): The URL of the API endpoint to be called.
            erc(int): The expected response code that should be returned by the
                DNA Center API endpoint to indicate success.
            **kwargs: Passed on to the requests package.

        Raises:
            ApiError: If anything other than the expected response code is
                returned by the DNA Center API endpoint.

        """
        # Ensure the url is an absolute URL
        abs_url = self.abs_url(url)

        # Update request kwargs with session defaults
        kwargs.setdefault('timeout', self.single_request_timeout)
        kwargs.setdefault('verify', self.verify)

        while True:
            # Make the HTTP request to the API endpoint
            response = self._req_session.request(method, abs_url, **kwargs)

            try:
                # Check the response code for error conditions
                check_response_code(response, erc)
            except RateLimitError as e:
                # Catch rate-limit errors
                # Wait and retry if automatic rate-limit handling is enabled
                if self.wait_on_rate_limit:
                    warnings.warn(RateLimitWarning(response))
                    time.sleep(e.retry_after)
                    continue
                else:
                    # Re-raise the RateLimitError
                    raise
            else:
                return response

    def download_file(self, file_name, content):
        try:
            f = open(file_name, 'w+')
            f.write(content)
            f.close()
        except Exception as e:
            raise DownloadFailure('Could not create/write to {}. Reason: {}'.format(file_name, e.message))
    

    def get(self, url, params=None, **kwargs):
        """Sends a GET request.

        Args:
            url(basestring): The URL of the API endpoint.
            params(dict): The parameters for the HTTP GET request.
            **kwargs:
                erc(int): The expected (success) response code for the request.
                others: Passed on to the requests package.

        Raises:
            ApiError: If anything other than the expected response code is
                returned by the DNA Center API endpoint.

        """
        check_type(url, basestring, may_be_none=False)
        check_type(params, dict)

        # Expected response code
        erc = kwargs.pop('erc', EXPECTED_RESPONSE_CODE['GET'])

        response = self.request('GET', url, erc, params=params, **kwargs)
        if 'fileName' in response.headers:
            file_name = response.headers.get('fileName')
            self.download_file(file_name, response.text)
        elif 'Content-Disposition' in response.headers:
            file_name = self.get_filename_from_cd(response.headers.get('Content-Disposition')).replace('"', '')
            self.download_file(file_name, response.text)
        return extract_and_parse_json(response)


    def post(self, url, params=None, json=None, data=None, **kwargs):
        """Sends a POST request.

        Args:
            url(basestring): The URL of the API endpoint.
            json: Data to be sent in JSON format in tbe body of the request.
            data: Data to be sent in the body of the request.
            **kwargs:
                erc(int): The expected (success) response code for the request.
                others: Passed on to the requests package.

        Raises:
            ApiError: If anything other than the expected response code is
                returned by the DNA Center API endpoint.

        """
        check_type(url, basestring, may_be_none=False)
        check_type(params, dict)

        # Expected response code
        erc = kwargs.pop('erc', EXPECTED_RESPONSE_CODE['POST'])

        response = self.request('POST', url, erc, params=params, json=json, data=data,
                                **kwargs)
        return extract_and_parse_json(response)

    def put(self, url, params=None, json=None, data=None, **kwargs):
        """Sends a PUT request.

        Args:
            url(basestring): The URL of the API endpoint.
            json: Data to be sent in JSON format in tbe body of the request.
            data: Data to be sent in the body of the request.
            **kwargs:
                erc(int): The expected (success) response code for the request.
                others: Passed on to the requests package.

        Raises:
            ApiError: If anything other than the expected response code is
                returned by the DNA Center API endpoint.

        """
        check_type(url, basestring, may_be_none=False)
        check_type(params, dict)

        # Expected response code
        erc = kwargs.pop('erc', EXPECTED_RESPONSE_CODE['PUT'])

        response = self.request('PUT', url, erc, params=params, json=json, data=data,
                                **kwargs)
        return extract_and_parse_json(response)

    def delete(self, url, params=None, **kwargs):
        """Sends a DELETE request.

        Args:
            url(basestring): The URL of the API endpoint.
            **kwargs:
                erc(int): The expected (success) response code for the request.
                others: Passed on to the requests package.

        Raises:
            ApiError: If anything other than the expected response code is
                returned by the DNA Center API endpoint.

        """
        check_type(url, basestring, may_be_none=False)
        check_type(params, dict)

        # Expected response code
        erc = kwargs.pop('erc', EXPECTED_RESPONSE_CODE['DELETE'])

        response =  self.request('DELETE', url, erc, params=params, **kwargs)
        return extract_and_parse_json(response)