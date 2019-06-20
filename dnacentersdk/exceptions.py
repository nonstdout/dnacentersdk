# -*- coding: utf-8 -*-
"""Package exceptions.

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

import logging
from builtins import *

import requests

from .response_codes import RESPONSE_CODES


logger = logging.getLogger(__name__)


class dnacentersdkException(Exception):
    """Base class for all dnacentersdk package exceptions."""
    pass


class AccessTokenError(dnacentersdkException):
    """Raised when an incorrect DNA Center Access Token has been provided."""
    pass


class ApiError(dnacentersdkException):
    """Errors returned in response to requests sent to the DNA Center APIs.

    Several data attributes are available for inspection.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended exception attributes
        self.response = response
        """The :class:`requests.Response` object returned from the API call."""

        self.request = self.response.request
        """The :class:`requests.PreparedRequest` of the API call."""

        self.status_code = self.response.status_code
        """The HTTP status code from the API response."""

        self.status = self.response.reason
        """The HTTP status from the API response."""

        self.details = None
        """The parsed JSON details from the API response."""
        if "application/json" in \
                self.response.headers.get("Content-Type", "").lower():
            try:
                self.details = self.response.json()
            except ValueError:
                logger.warning("Error parsing JSON response body")

        self.message = self.details.get("message") if self.details else None
        """The error message from the parsed API response."""

        self.description = RESPONSE_CODES.get(self.status_code)
        """A description of the HTTP Response Code from the API docs."""

        super(ApiError, self).__init__(
            "[{status_code}]{status} - {message}".format(
                status_code=self.status_code,
                status=" " + self.status if self.status else "",
                message=self.message or self.description or "Unknown Error",
            )
        )

    def __repr__(self):
        return "<{exception_name} [{status_code}]>".format(
            exception_name=self.__class__.__name__,
            status_code=self.status_code,
        )


class RateLimitError(ApiError):
    """DNA Center Rate-Limit exceeded Error.

    Raised when a rate-limit exceeded message is received and the request
    **will not** be retried.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended exception attributes
        self.retry_after = max(1, int(response.headers.get('Retry-After', 15)))
        """The `Retry-After` time period (in seconds) provided by DNA Center.

        Defaults to 15 seconds if the response `Retry-After` header isn't
        present in the response headers, and defaults to a minimum wait time of
        1 second if DNA Center returns a `Retry-After` header of 0 seconds.
        """

        super(RateLimitError, self).__init__(response)


class RateLimitWarning(UserWarning):
    """DNA Center rate-limit exceeded warning.

    Raised when a rate-limit exceeded message is received and the request will
    be retried.
    """

    def __init__(self, response):
        assert isinstance(response, requests.Response)

        # Extended warning attributes
        self.retry_after = max(1, int(response.headers.get('Retry-After', 15)))
        """The `Retry-After` time period (in seconds) provided by DNA Center.

        Defaults to 15 seconds if the response `Retry-After` header isn't
        present in the response headers, and defaults to a minimum wait time of
        1 second if DNA Center returns a `Retry-After` header of 0 seconds.
        """

        super(RateLimitWarning, self).__init__()


class MalformedResponse(dnacentersdkException):
    """Raised when a malformed response is received from DNA Center."""
    pass


class MalformedRequest(dnacentersdkException):
    """Raised when a malformed request is received from DNA Center user."""
    pass

class DownloadFailure(dnacentersdkException):
    """Raised when download operation was not successful."""
    pass