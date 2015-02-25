"""
    Base class of all resources.

    :copyright: © 2015 by Petr Zemek <s3rvac@gmail.com> and contributors
    :license: MIT, see the ``LICENSE`` file for more details
"""


class Resource:
    """Base class of all resources."""

    def __init__(self, id, conn):
        """Initializes the resource.

        :param str id: Unique identifier of the resource.
        :param retdec.conn.APIConnection conn: Connection to the API to be used
                                               for sending API requests.
        """
        self._id = id
        self._conn = conn

    @property
    def id(self):
        """Unique identifier of the resource."""
        return self._id
