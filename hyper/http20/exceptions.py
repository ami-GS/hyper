# -*- coding: utf-8 -*-
"""
hyper/http20/exceptions
~~~~~~~~~~~~~~~~~~~~~~~

This defines exceptions used in the HTTP/2.0 portion of hyper.
"""
class HTTP20Error(Exception):
    """
    The base class for all of ``hyper``'s HTTP/2.0-related exceptions.
    """
    pass


class HPACKEncodingError(HTTP20Error):
    """
    An error has been encountered while performing HPACK encoding.
    """
    pass


class HPACKDecodingError(HTTP20Error):
    """
    An error has been encountered while performing HPACK decoding.
    """
    pass

class ConnectionError(HTTP20Error):
    """
    The remote party signalled an error affecting the entire HTTP/2.0
    connection, and the connection has been closed.
    """
    pass
