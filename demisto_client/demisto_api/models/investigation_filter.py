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

from demisto_client.demisto_api.models.duration import Duration  # noqa: F401,E501
from demisto_client.demisto_api.models.investigation_status import InvestigationStatus  # noqa: F401,E501
from demisto_client.demisto_api.models.investigation_type import InvestigationType  # noqa: F401,E501
from demisto_client.demisto_api.models.order import Order  # noqa: F401,E501
from demisto_client.demisto_api.models.period import Period  # noqa: F401,E501


class InvestigationFilter(object):
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
        'cache': 'dict(str, list[str])',
        'and_op': 'bool',
        'category': 'list[str]',
        'from_close_date': 'datetime',
        'from_date': 'datetime',
        'from_date_license': 'datetime',
        'id': 'list[str]',
        'ids_only': 'bool',
        'ignore_workers': 'bool',
        'include_child_inv': 'bool',
        'name': 'list[str]',
        'not_category': 'list[str]',
        'not_i_ds': 'list[str]',
        'page': 'int',
        'period': 'Period',
        'reason': 'list[str]',
        'search_after': 'list[str]',
        'search_before': 'list[str]',
        'size': 'int',
        'sort': 'list[Order]',
        'status': 'list[InvestigationStatus]',
        'time_frame': 'Duration',
        'to_close_date': 'datetime',
        'to_date': 'datetime',
        'type': 'list[InvestigationType]',
        'user': 'list[str]'
    }

    attribute_map = {
        'cache': 'Cache',
        'and_op': 'andOp',
        'category': 'category',
        'from_close_date': 'fromCloseDate',
        'from_date': 'fromDate',
        'from_date_license': 'fromDateLicense',
        'id': 'id',
        'ids_only': 'idsOnly',
        'ignore_workers': 'ignoreWorkers',
        'include_child_inv': 'includeChildInv',
        'name': 'name',
        'not_category': 'notCategory',
        'not_i_ds': 'notIDs',
        'page': 'page',
        'period': 'period',
        'reason': 'reason',
        'search_after': 'searchAfter',
        'search_before': 'searchBefore',
        'size': 'size',
        'sort': 'sort',
        'status': 'status',
        'time_frame': 'timeFrame',
        'to_close_date': 'toCloseDate',
        'to_date': 'toDate',
        'type': 'type',
        'user': 'user'
    }

    def __init__(self, cache=None, and_op=None, category=None, from_close_date=None, from_date=None, from_date_license=None, id=None, ids_only=None, ignore_workers=None, include_child_inv=None, name=None, not_category=None, not_i_ds=None, page=None, period=None, reason=None, search_after=None, search_before=None, size=None, sort=None, status=None, time_frame=None, to_close_date=None, to_date=None, type=None, user=None):  # noqa: E501
        """InvestigationFilter - a model defined in Swagger"""  # noqa: E501

        self._cache = None
        self._and_op = None
        self._category = None
        self._from_close_date = None
        self._from_date = None
        self._from_date_license = None
        self._id = None
        self._ids_only = None
        self._ignore_workers = None
        self._include_child_inv = None
        self._name = None
        self._not_category = None
        self._not_i_ds = None
        self._page = None
        self._period = None
        self._reason = None
        self._search_after = None
        self._search_before = None
        self._size = None
        self._sort = None
        self._status = None
        self._time_frame = None
        self._to_close_date = None
        self._to_date = None
        self._type = None
        self._user = None
        self.discriminator = None

        if cache is not None:
            self.cache = cache
        if and_op is not None:
            self.and_op = and_op
        if category is not None:
            self.category = category
        if from_close_date is not None:
            self.from_close_date = from_close_date
        if from_date is not None:
            self.from_date = from_date
        if from_date_license is not None:
            self.from_date_license = from_date_license
        if id is not None:
            self.id = id
        if ids_only is not None:
            self.ids_only = ids_only
        if ignore_workers is not None:
            self.ignore_workers = ignore_workers
        if include_child_inv is not None:
            self.include_child_inv = include_child_inv
        if name is not None:
            self.name = name
        if not_category is not None:
            self.not_category = not_category
        if not_i_ds is not None:
            self.not_i_ds = not_i_ds
        if page is not None:
            self.page = page
        if period is not None:
            self.period = period
        if reason is not None:
            self.reason = reason
        if search_after is not None:
            self.search_after = search_after
        if search_before is not None:
            self.search_before = search_before
        if size is not None:
            self.size = size
        if sort is not None:
            self.sort = sort
        if status is not None:
            self.status = status
        if time_frame is not None:
            self.time_frame = time_frame
        if to_close_date is not None:
            self.to_close_date = to_close_date
        if to_date is not None:
            self.to_date = to_date
        if type is not None:
            self.type = type
        if user is not None:
            self.user = user

    @property
    def cache(self):
        """Gets the cache of this InvestigationFilter.  # noqa: E501

        Cache of join functions  # noqa: E501

        :return: The cache of this InvestigationFilter.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._cache

    @cache.setter
    def cache(self, cache):
        """Sets the cache of this InvestigationFilter.

        Cache of join functions  # noqa: E501

        :param cache: The cache of this InvestigationFilter.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._cache = cache

    @property
    def and_op(self):
        """Gets the and_op of this InvestigationFilter.  # noqa: E501


        :return: The and_op of this InvestigationFilter.  # noqa: E501
        :rtype: bool
        """
        return self._and_op

    @and_op.setter
    def and_op(self, and_op):
        """Sets the and_op of this InvestigationFilter.


        :param and_op: The and_op of this InvestigationFilter.  # noqa: E501
        :type: bool
        """

        self._and_op = and_op

    @property
    def category(self):
        """Gets the category of this InvestigationFilter.  # noqa: E501


        :return: The category of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InvestigationFilter.


        :param category: The category of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._category = category

    @property
    def from_close_date(self):
        """Gets the from_close_date of this InvestigationFilter.  # noqa: E501


        :return: The from_close_date of this InvestigationFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_close_date

    @from_close_date.setter
    def from_close_date(self, from_close_date):
        """Sets the from_close_date of this InvestigationFilter.


        :param from_close_date: The from_close_date of this InvestigationFilter.  # noqa: E501
        :type: datetime
        """

        self._from_close_date = from_close_date

    @property
    def from_date(self):
        """Gets the from_date of this InvestigationFilter.  # noqa: E501


        :return: The from_date of this InvestigationFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this InvestigationFilter.


        :param from_date: The from_date of this InvestigationFilter.  # noqa: E501
        :type: datetime
        """

        self._from_date = from_date

    @property
    def from_date_license(self):
        """Gets the from_date_license of this InvestigationFilter.  # noqa: E501


        :return: The from_date_license of this InvestigationFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._from_date_license

    @from_date_license.setter
    def from_date_license(self, from_date_license):
        """Sets the from_date_license of this InvestigationFilter.


        :param from_date_license: The from_date_license of this InvestigationFilter.  # noqa: E501
        :type: datetime
        """

        self._from_date_license = from_date_license

    @property
    def id(self):
        """Gets the id of this InvestigationFilter.  # noqa: E501


        :return: The id of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvestigationFilter.


        :param id: The id of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._id = id

    @property
    def ids_only(self):
        """Gets the ids_only of this InvestigationFilter.  # noqa: E501


        :return: The ids_only of this InvestigationFilter.  # noqa: E501
        :rtype: bool
        """
        return self._ids_only

    @ids_only.setter
    def ids_only(self, ids_only):
        """Sets the ids_only of this InvestigationFilter.


        :param ids_only: The ids_only of this InvestigationFilter.  # noqa: E501
        :type: bool
        """

        self._ids_only = ids_only

    @property
    def ignore_workers(self):
        """Gets the ignore_workers of this InvestigationFilter.  # noqa: E501

        Do not use workers mechanism while searching bleve  # noqa: E501

        :return: The ignore_workers of this InvestigationFilter.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_workers

    @ignore_workers.setter
    def ignore_workers(self, ignore_workers):
        """Sets the ignore_workers of this InvestigationFilter.

        Do not use workers mechanism while searching bleve  # noqa: E501

        :param ignore_workers: The ignore_workers of this InvestigationFilter.  # noqa: E501
        :type: bool
        """

        self._ignore_workers = ignore_workers

    @property
    def include_child_inv(self):
        """Gets the include_child_inv of this InvestigationFilter.  # noqa: E501


        :return: The include_child_inv of this InvestigationFilter.  # noqa: E501
        :rtype: bool
        """
        return self._include_child_inv

    @include_child_inv.setter
    def include_child_inv(self, include_child_inv):
        """Sets the include_child_inv of this InvestigationFilter.


        :param include_child_inv: The include_child_inv of this InvestigationFilter.  # noqa: E501
        :type: bool
        """

        self._include_child_inv = include_child_inv

    @property
    def name(self):
        """Gets the name of this InvestigationFilter.  # noqa: E501


        :return: The name of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvestigationFilter.


        :param name: The name of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._name = name

    @property
    def not_category(self):
        """Gets the not_category of this InvestigationFilter.  # noqa: E501


        :return: The not_category of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_category

    @not_category.setter
    def not_category(self, not_category):
        """Sets the not_category of this InvestigationFilter.


        :param not_category: The not_category of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._not_category = not_category

    @property
    def not_i_ds(self):
        """Gets the not_i_ds of this InvestigationFilter.  # noqa: E501


        :return: The not_i_ds of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._not_i_ds

    @not_i_ds.setter
    def not_i_ds(self, not_i_ds):
        """Sets the not_i_ds of this InvestigationFilter.


        :param not_i_ds: The not_i_ds of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._not_i_ds = not_i_ds

    @property
    def page(self):
        """Gets the page of this InvestigationFilter.  # noqa: E501

        0-based page  # noqa: E501

        :return: The page of this InvestigationFilter.  # noqa: E501
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this InvestigationFilter.

        0-based page  # noqa: E501

        :param page: The page of this InvestigationFilter.  # noqa: E501
        :type: int
        """

        self._page = page

    @property
    def period(self):
        """Gets the period of this InvestigationFilter.  # noqa: E501


        :return: The period of this InvestigationFilter.  # noqa: E501
        :rtype: Period
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this InvestigationFilter.


        :param period: The period of this InvestigationFilter.  # noqa: E501
        :type: Period
        """

        self._period = period

    @property
    def reason(self):
        """Gets the reason of this InvestigationFilter.  # noqa: E501


        :return: The reason of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InvestigationFilter.


        :param reason: The reason of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._reason = reason

    @property
    def search_after(self):
        """Gets the search_after of this InvestigationFilter.  # noqa: E501

        Efficient next page, pass max sort value from previous page  # noqa: E501

        :return: The search_after of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_after

    @search_after.setter
    def search_after(self, search_after):
        """Sets the search_after of this InvestigationFilter.

        Efficient next page, pass max sort value from previous page  # noqa: E501

        :param search_after: The search_after of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._search_after = search_after

    @property
    def search_before(self):
        """Gets the search_before of this InvestigationFilter.  # noqa: E501

        Efficient prev page, pass min sort value from next page  # noqa: E501

        :return: The search_before of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_before

    @search_before.setter
    def search_before(self, search_before):
        """Sets the search_before of this InvestigationFilter.

        Efficient prev page, pass min sort value from next page  # noqa: E501

        :param search_before: The search_before of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._search_before = search_before

    @property
    def size(self):
        """Gets the size of this InvestigationFilter.  # noqa: E501

        Size is limited to 1000, if not passed it defaults to 0, and no results will return  # noqa: E501

        :return: The size of this InvestigationFilter.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InvestigationFilter.

        Size is limited to 1000, if not passed it defaults to 0, and no results will return  # noqa: E501

        :param size: The size of this InvestigationFilter.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def sort(self):
        """Gets the sort of this InvestigationFilter.  # noqa: E501

        The sort order  # noqa: E501

        :return: The sort of this InvestigationFilter.  # noqa: E501
        :rtype: list[Order]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this InvestigationFilter.

        The sort order  # noqa: E501

        :param sort: The sort of this InvestigationFilter.  # noqa: E501
        :type: list[Order]
        """

        self._sort = sort

    @property
    def status(self):
        """Gets the status of this InvestigationFilter.  # noqa: E501


        :return: The status of this InvestigationFilter.  # noqa: E501
        :rtype: list[InvestigationStatus]
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvestigationFilter.


        :param status: The status of this InvestigationFilter.  # noqa: E501
        :type: list[InvestigationStatus]
        """

        self._status = status

    @property
    def time_frame(self):
        """Gets the time_frame of this InvestigationFilter.  # noqa: E501


        :return: The time_frame of this InvestigationFilter.  # noqa: E501
        :rtype: Duration
        """
        return self._time_frame

    @time_frame.setter
    def time_frame(self, time_frame):
        """Sets the time_frame of this InvestigationFilter.


        :param time_frame: The time_frame of this InvestigationFilter.  # noqa: E501
        :type: Duration
        """

        self._time_frame = time_frame

    @property
    def to_close_date(self):
        """Gets the to_close_date of this InvestigationFilter.  # noqa: E501


        :return: The to_close_date of this InvestigationFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_close_date

    @to_close_date.setter
    def to_close_date(self, to_close_date):
        """Sets the to_close_date of this InvestigationFilter.


        :param to_close_date: The to_close_date of this InvestigationFilter.  # noqa: E501
        :type: datetime
        """

        self._to_close_date = to_close_date

    @property
    def to_date(self):
        """Gets the to_date of this InvestigationFilter.  # noqa: E501


        :return: The to_date of this InvestigationFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this InvestigationFilter.


        :param to_date: The to_date of this InvestigationFilter.  # noqa: E501
        :type: datetime
        """

        self._to_date = to_date

    @property
    def type(self):
        """Gets the type of this InvestigationFilter.  # noqa: E501


        :return: The type of this InvestigationFilter.  # noqa: E501
        :rtype: list[InvestigationType]
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvestigationFilter.


        :param type: The type of this InvestigationFilter.  # noqa: E501
        :type: list[InvestigationType]
        """

        self._type = type

    @property
    def user(self):
        """Gets the user of this InvestigationFilter.  # noqa: E501


        :return: The user of this InvestigationFilter.  # noqa: E501
        :rtype: list[str]
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this InvestigationFilter.


        :param user: The user of this InvestigationFilter.  # noqa: E501
        :type: list[str]
        """

        self._user = user

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
        if issubclass(InvestigationFilter, dict):
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
        if not isinstance(other, InvestigationFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
