# coding: utf-8

"""
    Cortex XSOAR API

    This is the public REST API to integrate with the Cortex XSOAR server. HTTP request can be sent using any HTTP-client.  For an example dedicated client take a look at: https://github.com/demisto/demisto-py.  Requests must include API-key that can be generated in the Cortex XSOAR web client under 'Settings' -> 'Integrations' -> 'API keys'   Optimistic Locking and Versioning\\:  When using Cortex XSOAR REST API, you will need to make sure to work on the latest version of the item (incident, entry, etc.), otherwise, you will get a DB version error (which not allow you to override a newer item). In addition, you can pass 'version\\: -1' to force data override (make sure that other users data might be lost).  Assume that Alice and Bob both read the same data from Cortex XSOAR server, then they both changed the data, and then both tried to write the new versions back to the server. Whose changes should be saved? Alice’s? Bob’s? To solve this, each data item in Cortex XSOAR has a numeric incremental version. If Alice saved an item with version 4 and Bob trying to save the same item with version 3, Cortex XSOAR will rollback Bob request and returns a DB version conflict error. Bob will need to get the latest item and work on it so Alice work will not get lost.  Example request using 'curl'\\:  ``` curl 'https://hostname:443/incidents/search' -H 'content-type: application/json' -H 'accept: application/json' -H 'Authorization: <API Key goes here>' --data-binary '{\"filter\":{\"query\":\"-status:closed -category:job\",\"period\":{\"by\":\"day\",\"fromValue\":7}}}' --compressed ```  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class DBotScore(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'content': 'str',
        'content_format': 'str',
        'context': 'dict(str, object)',
        'is_typed_indicator': 'bool',
        'score': 'int',
        'score_change_timestamp': 'datetime',
        'timestamp': 'datetime',
        'type': 'str'
    }

    attribute_map = {
        'content': 'content',
        'content_format': 'contentFormat',
        'context': 'context',
        'is_typed_indicator': 'isTypedIndicator',
        'score': 'score',
        'score_change_timestamp': 'scoreChangeTimestamp',
        'timestamp': 'timestamp',
        'type': 'type'
    }

    def __init__(self, content=None, content_format=None, context=None, is_typed_indicator=None, score=None, score_change_timestamp=None, timestamp=None, type=None):  # noqa: E501
        """DBotScore - a model defined in Swagger"""  # noqa: E501

        self._content = None
        self._content_format = None
        self._context = None
        self._is_typed_indicator = None
        self._score = None
        self._score_change_timestamp = None
        self._timestamp = None
        self._type = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if content_format is not None:
            self.content_format = content_format
        if context is not None:
            self.context = context
        if is_typed_indicator is not None:
            self.is_typed_indicator = is_typed_indicator
        if score is not None:
            self.score = score
        if score_change_timestamp is not None:
            self.score_change_timestamp = score_change_timestamp
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type

    @property
    def content(self):
        """Gets the content of this DBotScore.  # noqa: E501


        :return: The content of this DBotScore.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this DBotScore.


        :param content: The content of this DBotScore.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_format(self):
        """Gets the content_format of this DBotScore.  # noqa: E501


        :return: The content_format of this DBotScore.  # noqa: E501
        :rtype: str
        """
        return self._content_format

    @content_format.setter
    def content_format(self, content_format):
        """Sets the content_format of this DBotScore.


        :param content_format: The content_format of this DBotScore.  # noqa: E501
        :type: str
        """

        self._content_format = content_format

    @property
    def context(self):
        """Gets the context of this DBotScore.  # noqa: E501


        :return: The context of this DBotScore.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this DBotScore.


        :param context: The context of this DBotScore.  # noqa: E501
        :type: dict(str, object)
        """

        self._context = context

    @property
    def is_typed_indicator(self):
        """Gets the is_typed_indicator of this DBotScore.  # noqa: E501


        :return: The is_typed_indicator of this DBotScore.  # noqa: E501
        :rtype: bool
        """
        return self._is_typed_indicator

    @is_typed_indicator.setter
    def is_typed_indicator(self, is_typed_indicator):
        """Sets the is_typed_indicator of this DBotScore.


        :param is_typed_indicator: The is_typed_indicator of this DBotScore.  # noqa: E501
        :type: bool
        """

        self._is_typed_indicator = is_typed_indicator

    @property
    def score(self):
        """Gets the score of this DBotScore.  # noqa: E501


        :return: The score of this DBotScore.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DBotScore.


        :param score: The score of this DBotScore.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def score_change_timestamp(self):
        """Gets the score_change_timestamp of this DBotScore.  # noqa: E501

        We need to track when the score changes to know if we need to re-calculate the overall score  # noqa: E501

        :return: The score_change_timestamp of this DBotScore.  # noqa: E501
        :rtype: datetime
        """
        return self._score_change_timestamp

    @score_change_timestamp.setter
    def score_change_timestamp(self, score_change_timestamp):
        """Sets the score_change_timestamp of this DBotScore.

        We need to track when the score changes to know if we need to re-calculate the overall score  # noqa: E501

        :param score_change_timestamp: The score_change_timestamp of this DBotScore.  # noqa: E501
        :type: datetime
        """

        self._score_change_timestamp = score_change_timestamp

    @property
    def timestamp(self):
        """Gets the timestamp of this DBotScore.  # noqa: E501


        :return: The timestamp of this DBotScore.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this DBotScore.


        :param timestamp: The timestamp of this DBotScore.  # noqa: E501
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this DBotScore.  # noqa: E501


        :return: The type of this DBotScore.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DBotScore.


        :param type: The type of this DBotScore.  # noqa: E501
        :type: str
        """

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(DBotScore, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DBotScore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
