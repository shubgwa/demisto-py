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

from demisto_client.demisto_api.models.investigation_playbook_data import InvestigationPlaybookData  # noqa: F401,E501
from demisto_client.demisto_api.models.investigation_playbook_state import InvestigationPlaybookState  # noqa: F401,E501
from demisto_client.demisto_api.models.investigation_playbook_task import InvestigationPlaybookTask  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_inputs import PlaybookInputs  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_outputs import PlaybookOutputs  # noqa: F401,E501
from demisto_client.demisto_api.models.playbook_view import PlaybookView  # noqa: F401,E501


class InvestigationPlaybook(object):
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
        'dirty': 'bool',
        'ready_playbook_inputs': 'dict(str, dict(str, object))',
        'replaced_playbook': 'bool',
        'shard_id': 'int',
        'updated_operator_i_ds': 'bool',
        'auto_extracting': 'bool',
        'comment': 'str',
        'dbot_created_by': 'str',
        'has_role': 'bool',
        'id': 'str',
        'incident_create_date': 'datetime',
        'inputs': 'PlaybookInputs',
        'investigation_id': 'str',
        'is_tim': 'bool',
        'modified': 'datetime',
        'name': 'str',
        'outputs': 'PlaybookOutputs',
        'pb_history': 'list[InvestigationPlaybookData]',
        'playbook_id': 'str',
        'previous_roles': 'list[str]',
        'primary_term': 'int',
        'quiet': 'bool',
        'roles': 'list[str]',
        'sequence_number': 'int',
        'server_id': 'str',
        'sort_values': 'list[str]',
        'start_date': 'datetime',
        'start_task_id': 'str',
        'state': 'InvestigationPlaybookState',
        'sub_playbook_inputs': 'dict(str, PlaybookInputs)',
        'sub_playbook_outputs': 'dict(str, PlaybookOutputs)',
        'tasks': 'dict(str, InvestigationPlaybookTask)',
        'version': 'int',
        'view': 'PlaybookView'
    }

    attribute_map = {
        'dirty': 'Dirty',
        'ready_playbook_inputs': 'ReadyPlaybookInputs',
        'replaced_playbook': 'ReplacedPlaybook',
        'shard_id': 'ShardID',
        'updated_operator_i_ds': 'UpdatedOperatorIDs',
        'auto_extracting': 'autoExtracting',
        'comment': 'comment',
        'dbot_created_by': 'dbotCreatedBy',
        'has_role': 'hasRole',
        'id': 'id',
        'incident_create_date': 'incidentCreateDate',
        'inputs': 'inputs',
        'investigation_id': 'investigationId',
        'is_tim': 'isTIM',
        'modified': 'modified',
        'name': 'name',
        'outputs': 'outputs',
        'pb_history': 'pbHistory',
        'playbook_id': 'playbookId',
        'previous_roles': 'previousRoles',
        'primary_term': 'primaryTerm',
        'quiet': 'quiet',
        'roles': 'roles',
        'sequence_number': 'sequenceNumber',
        'server_id': 'serverId',
        'sort_values': 'sortValues',
        'start_date': 'startDate',
        'start_task_id': 'startTaskId',
        'state': 'state',
        'sub_playbook_inputs': 'subPlaybookInputs',
        'sub_playbook_outputs': 'subPlaybookOutputs',
        'tasks': 'tasks',
        'version': 'version',
        'view': 'view'
    }

    def __init__(self, dirty=None, ready_playbook_inputs=None, replaced_playbook=None, shard_id=None, updated_operator_i_ds=None, auto_extracting=None, comment=None, dbot_created_by=None, has_role=None, id=None, incident_create_date=None, inputs=None, investigation_id=None, is_tim=None, modified=None, name=None, outputs=None, pb_history=None, playbook_id=None, previous_roles=None, primary_term=None, quiet=None, roles=None, sequence_number=None, server_id=None, sort_values=None, start_date=None, start_task_id=None, state=None, sub_playbook_inputs=None, sub_playbook_outputs=None, tasks=None, version=None, view=None):  # noqa: E501
        """InvestigationPlaybook - a model defined in Swagger"""  # noqa: E501

        self._dirty = None
        self._ready_playbook_inputs = None
        self._replaced_playbook = None
        self._shard_id = None
        self._updated_operator_i_ds = None
        self._auto_extracting = None
        self._comment = None
        self._dbot_created_by = None
        self._has_role = None
        self._id = None
        self._incident_create_date = None
        self._inputs = None
        self._investigation_id = None
        self._is_tim = None
        self._modified = None
        self._name = None
        self._outputs = None
        self._pb_history = None
        self._playbook_id = None
        self._previous_roles = None
        self._primary_term = None
        self._quiet = None
        self._roles = None
        self._sequence_number = None
        self._server_id = None
        self._sort_values = None
        self._start_date = None
        self._start_task_id = None
        self._state = None
        self._sub_playbook_inputs = None
        self._sub_playbook_outputs = None
        self._tasks = None
        self._version = None
        self._view = None
        self.discriminator = None

        if dirty is not None:
            self.dirty = dirty
        if ready_playbook_inputs is not None:
            self.ready_playbook_inputs = ready_playbook_inputs
        if replaced_playbook is not None:
            self.replaced_playbook = replaced_playbook
        if shard_id is not None:
            self.shard_id = shard_id
        if updated_operator_i_ds is not None:
            self.updated_operator_i_ds = updated_operator_i_ds
        if auto_extracting is not None:
            self.auto_extracting = auto_extracting
        if comment is not None:
            self.comment = comment
        if dbot_created_by is not None:
            self.dbot_created_by = dbot_created_by
        if has_role is not None:
            self.has_role = has_role
        if id is not None:
            self.id = id
        if incident_create_date is not None:
            self.incident_create_date = incident_create_date
        if inputs is not None:
            self.inputs = inputs
        if investigation_id is not None:
            self.investigation_id = investigation_id
        if is_tim is not None:
            self.is_tim = is_tim
        if modified is not None:
            self.modified = modified
        if name is not None:
            self.name = name
        if outputs is not None:
            self.outputs = outputs
        if pb_history is not None:
            self.pb_history = pb_history
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if previous_roles is not None:
            self.previous_roles = previous_roles
        if primary_term is not None:
            self.primary_term = primary_term
        if quiet is not None:
            self.quiet = quiet
        if roles is not None:
            self.roles = roles
        if sequence_number is not None:
            self.sequence_number = sequence_number
        if server_id is not None:
            self.server_id = server_id
        if sort_values is not None:
            self.sort_values = sort_values
        if start_date is not None:
            self.start_date = start_date
        if start_task_id is not None:
            self.start_task_id = start_task_id
        if state is not None:
            self.state = state
        if sub_playbook_inputs is not None:
            self.sub_playbook_inputs = sub_playbook_inputs
        if sub_playbook_outputs is not None:
            self.sub_playbook_outputs = sub_playbook_outputs
        if tasks is not None:
            self.tasks = tasks
        if version is not None:
            self.version = version
        if view is not None:
            self.view = view

    @property
    def dirty(self):
        """Gets the dirty of this InvestigationPlaybook.  # noqa: E501


        :return: The dirty of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._dirty

    @dirty.setter
    def dirty(self, dirty):
        """Sets the dirty of this InvestigationPlaybook.


        :param dirty: The dirty of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._dirty = dirty

    @property
    def ready_playbook_inputs(self):
        """Gets the ready_playbook_inputs of this InvestigationPlaybook.  # noqa: E501


        :return: The ready_playbook_inputs of this InvestigationPlaybook.  # noqa: E501
        :rtype: dict(str, dict(str, object))
        """
        return self._ready_playbook_inputs

    @ready_playbook_inputs.setter
    def ready_playbook_inputs(self, ready_playbook_inputs):
        """Sets the ready_playbook_inputs of this InvestigationPlaybook.


        :param ready_playbook_inputs: The ready_playbook_inputs of this InvestigationPlaybook.  # noqa: E501
        :type: dict(str, dict(str, object))
        """

        self._ready_playbook_inputs = ready_playbook_inputs

    @property
    def replaced_playbook(self):
        """Gets the replaced_playbook of this InvestigationPlaybook.  # noqa: E501

        Indicate whether this playbook has new history during this session  # noqa: E501

        :return: The replaced_playbook of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._replaced_playbook

    @replaced_playbook.setter
    def replaced_playbook(self, replaced_playbook):
        """Sets the replaced_playbook of this InvestigationPlaybook.

        Indicate whether this playbook has new history during this session  # noqa: E501

        :param replaced_playbook: The replaced_playbook of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._replaced_playbook = replaced_playbook

    @property
    def shard_id(self):
        """Gets the shard_id of this InvestigationPlaybook.  # noqa: E501


        :return: The shard_id of this InvestigationPlaybook.  # noqa: E501
        :rtype: int
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        """Sets the shard_id of this InvestigationPlaybook.


        :param shard_id: The shard_id of this InvestigationPlaybook.  # noqa: E501
        :type: int
        """

        self._shard_id = shard_id

    @property
    def updated_operator_i_ds(self):
        """Gets the updated_operator_i_ds of this InvestigationPlaybook.  # noqa: E501


        :return: The updated_operator_i_ds of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._updated_operator_i_ds

    @updated_operator_i_ds.setter
    def updated_operator_i_ds(self, updated_operator_i_ds):
        """Sets the updated_operator_i_ds of this InvestigationPlaybook.


        :param updated_operator_i_ds: The updated_operator_i_ds of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._updated_operator_i_ds = updated_operator_i_ds

    @property
    def auto_extracting(self):
        """Gets the auto_extracting of this InvestigationPlaybook.  # noqa: E501


        :return: The auto_extracting of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._auto_extracting

    @auto_extracting.setter
    def auto_extracting(self, auto_extracting):
        """Sets the auto_extracting of this InvestigationPlaybook.


        :param auto_extracting: The auto_extracting of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._auto_extracting = auto_extracting

    @property
    def comment(self):
        """Gets the comment of this InvestigationPlaybook.  # noqa: E501


        :return: The comment of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this InvestigationPlaybook.


        :param comment: The comment of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def dbot_created_by(self):
        """Gets the dbot_created_by of this InvestigationPlaybook.  # noqa: E501

        Who has created this event - relevant only for manual incidents  # noqa: E501

        :return: The dbot_created_by of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._dbot_created_by

    @dbot_created_by.setter
    def dbot_created_by(self, dbot_created_by):
        """Sets the dbot_created_by of this InvestigationPlaybook.

        Who has created this event - relevant only for manual incidents  # noqa: E501

        :param dbot_created_by: The dbot_created_by of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._dbot_created_by = dbot_created_by

    @property
    def has_role(self):
        """Gets the has_role of this InvestigationPlaybook.  # noqa: E501

        Internal field to make queries on role faster  # noqa: E501

        :return: The has_role of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._has_role

    @has_role.setter
    def has_role(self, has_role):
        """Sets the has_role of this InvestigationPlaybook.

        Internal field to make queries on role faster  # noqa: E501

        :param has_role: The has_role of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._has_role = has_role

    @property
    def id(self):
        """Gets the id of this InvestigationPlaybook.  # noqa: E501


        :return: The id of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvestigationPlaybook.


        :param id: The id of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def incident_create_date(self):
        """Gets the incident_create_date of this InvestigationPlaybook.  # noqa: E501

        Incident create date  # noqa: E501

        :return: The incident_create_date of this InvestigationPlaybook.  # noqa: E501
        :rtype: datetime
        """
        return self._incident_create_date

    @incident_create_date.setter
    def incident_create_date(self, incident_create_date):
        """Sets the incident_create_date of this InvestigationPlaybook.

        Incident create date  # noqa: E501

        :param incident_create_date: The incident_create_date of this InvestigationPlaybook.  # noqa: E501
        :type: datetime
        """

        self._incident_create_date = incident_create_date

    @property
    def inputs(self):
        """Gets the inputs of this InvestigationPlaybook.  # noqa: E501


        :return: The inputs of this InvestigationPlaybook.  # noqa: E501
        :rtype: PlaybookInputs
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        """Sets the inputs of this InvestigationPlaybook.


        :param inputs: The inputs of this InvestigationPlaybook.  # noqa: E501
        :type: PlaybookInputs
        """

        self._inputs = inputs

    @property
    def investigation_id(self):
        """Gets the investigation_id of this InvestigationPlaybook.  # noqa: E501


        :return: The investigation_id of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._investigation_id

    @investigation_id.setter
    def investigation_id(self, investigation_id):
        """Sets the investigation_id of this InvestigationPlaybook.


        :param investigation_id: The investigation_id of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._investigation_id = investigation_id

    @property
    def is_tim(self):
        """Gets the is_tim of this InvestigationPlaybook.  # noqa: E501


        :return: The is_tim of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._is_tim

    @is_tim.setter
    def is_tim(self, is_tim):
        """Sets the is_tim of this InvestigationPlaybook.


        :param is_tim: The is_tim of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._is_tim = is_tim

    @property
    def modified(self):
        """Gets the modified of this InvestigationPlaybook.  # noqa: E501


        :return: The modified of this InvestigationPlaybook.  # noqa: E501
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this InvestigationPlaybook.


        :param modified: The modified of this InvestigationPlaybook.  # noqa: E501
        :type: datetime
        """

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this InvestigationPlaybook.  # noqa: E501


        :return: The name of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InvestigationPlaybook.


        :param name: The name of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def outputs(self):
        """Gets the outputs of this InvestigationPlaybook.  # noqa: E501


        :return: The outputs of this InvestigationPlaybook.  # noqa: E501
        :rtype: PlaybookOutputs
        """
        return self._outputs

    @outputs.setter
    def outputs(self, outputs):
        """Sets the outputs of this InvestigationPlaybook.


        :param outputs: The outputs of this InvestigationPlaybook.  # noqa: E501
        :type: PlaybookOutputs
        """

        self._outputs = outputs

    @property
    def pb_history(self):
        """Gets the pb_history of this InvestigationPlaybook.  # noqa: E501

        in: body  # noqa: E501

        :return: The pb_history of this InvestigationPlaybook.  # noqa: E501
        :rtype: list[InvestigationPlaybookData]
        """
        return self._pb_history

    @pb_history.setter
    def pb_history(self, pb_history):
        """Sets the pb_history of this InvestigationPlaybook.

        in: body  # noqa: E501

        :param pb_history: The pb_history of this InvestigationPlaybook.  # noqa: E501
        :type: list[InvestigationPlaybookData]
        """

        self._pb_history = pb_history

    @property
    def playbook_id(self):
        """Gets the playbook_id of this InvestigationPlaybook.  # noqa: E501


        :return: The playbook_id of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this InvestigationPlaybook.


        :param playbook_id: The playbook_id of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._playbook_id = playbook_id

    @property
    def previous_roles(self):
        """Gets the previous_roles of this InvestigationPlaybook.  # noqa: E501

        PreviousRoleName - do not change this field manually  # noqa: E501

        :return: The previous_roles of this InvestigationPlaybook.  # noqa: E501
        :rtype: list[str]
        """
        return self._previous_roles

    @previous_roles.setter
    def previous_roles(self, previous_roles):
        """Sets the previous_roles of this InvestigationPlaybook.

        PreviousRoleName - do not change this field manually  # noqa: E501

        :param previous_roles: The previous_roles of this InvestigationPlaybook.  # noqa: E501
        :type: list[str]
        """

        self._previous_roles = previous_roles

    @property
    def primary_term(self):
        """Gets the primary_term of this InvestigationPlaybook.  # noqa: E501


        :return: The primary_term of this InvestigationPlaybook.  # noqa: E501
        :rtype: int
        """
        return self._primary_term

    @primary_term.setter
    def primary_term(self, primary_term):
        """Sets the primary_term of this InvestigationPlaybook.


        :param primary_term: The primary_term of this InvestigationPlaybook.  # noqa: E501
        :type: int
        """

        self._primary_term = primary_term

    @property
    def quiet(self):
        """Gets the quiet of this InvestigationPlaybook.  # noqa: E501


        :return: The quiet of this InvestigationPlaybook.  # noqa: E501
        :rtype: bool
        """
        return self._quiet

    @quiet.setter
    def quiet(self, quiet):
        """Sets the quiet of this InvestigationPlaybook.


        :param quiet: The quiet of this InvestigationPlaybook.  # noqa: E501
        :type: bool
        """

        self._quiet = quiet

    @property
    def roles(self):
        """Gets the roles of this InvestigationPlaybook.  # noqa: E501

        The role assigned to this investigation  # noqa: E501

        :return: The roles of this InvestigationPlaybook.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this InvestigationPlaybook.

        The role assigned to this investigation  # noqa: E501

        :param roles: The roles of this InvestigationPlaybook.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def sequence_number(self):
        """Gets the sequence_number of this InvestigationPlaybook.  # noqa: E501


        :return: The sequence_number of this InvestigationPlaybook.  # noqa: E501
        :rtype: int
        """
        return self._sequence_number

    @sequence_number.setter
    def sequence_number(self, sequence_number):
        """Sets the sequence_number of this InvestigationPlaybook.


        :param sequence_number: The sequence_number of this InvestigationPlaybook.  # noqa: E501
        :type: int
        """

        self._sequence_number = sequence_number

    @property
    def server_id(self):
        """Gets the server_id of this InvestigationPlaybook.  # noqa: E501

        Holds the ID of the responsible cluster app server  # noqa: E501

        :return: The server_id of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this InvestigationPlaybook.

        Holds the ID of the responsible cluster app server  # noqa: E501

        :param server_id: The server_id of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._server_id = server_id

    @property
    def sort_values(self):
        """Gets the sort_values of this InvestigationPlaybook.  # noqa: E501


        :return: The sort_values of this InvestigationPlaybook.  # noqa: E501
        :rtype: list[str]
        """
        return self._sort_values

    @sort_values.setter
    def sort_values(self, sort_values):
        """Sets the sort_values of this InvestigationPlaybook.


        :param sort_values: The sort_values of this InvestigationPlaybook.  # noqa: E501
        :type: list[str]
        """

        self._sort_values = sort_values

    @property
    def start_date(self):
        """Gets the start_date of this InvestigationPlaybook.  # noqa: E501


        :return: The start_date of this InvestigationPlaybook.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this InvestigationPlaybook.


        :param start_date: The start_date of this InvestigationPlaybook.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def start_task_id(self):
        """Gets the start_task_id of this InvestigationPlaybook.  # noqa: E501

        FirstTask is the root task of the playbook  # noqa: E501

        :return: The start_task_id of this InvestigationPlaybook.  # noqa: E501
        :rtype: str
        """
        return self._start_task_id

    @start_task_id.setter
    def start_task_id(self, start_task_id):
        """Sets the start_task_id of this InvestigationPlaybook.

        FirstTask is the root task of the playbook  # noqa: E501

        :param start_task_id: The start_task_id of this InvestigationPlaybook.  # noqa: E501
        :type: str
        """

        self._start_task_id = start_task_id

    @property
    def state(self):
        """Gets the state of this InvestigationPlaybook.  # noqa: E501


        :return: The state of this InvestigationPlaybook.  # noqa: E501
        :rtype: InvestigationPlaybookState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvestigationPlaybook.


        :param state: The state of this InvestigationPlaybook.  # noqa: E501
        :type: InvestigationPlaybookState
        """

        self._state = state

    @property
    def sub_playbook_inputs(self):
        """Gets the sub_playbook_inputs of this InvestigationPlaybook.  # noqa: E501


        :return: The sub_playbook_inputs of this InvestigationPlaybook.  # noqa: E501
        :rtype: dict(str, PlaybookInputs)
        """
        return self._sub_playbook_inputs

    @sub_playbook_inputs.setter
    def sub_playbook_inputs(self, sub_playbook_inputs):
        """Sets the sub_playbook_inputs of this InvestigationPlaybook.


        :param sub_playbook_inputs: The sub_playbook_inputs of this InvestigationPlaybook.  # noqa: E501
        :type: dict(str, PlaybookInputs)
        """

        self._sub_playbook_inputs = sub_playbook_inputs

    @property
    def sub_playbook_outputs(self):
        """Gets the sub_playbook_outputs of this InvestigationPlaybook.  # noqa: E501


        :return: The sub_playbook_outputs of this InvestigationPlaybook.  # noqa: E501
        :rtype: dict(str, PlaybookOutputs)
        """
        return self._sub_playbook_outputs

    @sub_playbook_outputs.setter
    def sub_playbook_outputs(self, sub_playbook_outputs):
        """Sets the sub_playbook_outputs of this InvestigationPlaybook.


        :param sub_playbook_outputs: The sub_playbook_outputs of this InvestigationPlaybook.  # noqa: E501
        :type: dict(str, PlaybookOutputs)
        """

        self._sub_playbook_outputs = sub_playbook_outputs

    @property
    def tasks(self):
        """Gets the tasks of this InvestigationPlaybook.  # noqa: E501


        :return: The tasks of this InvestigationPlaybook.  # noqa: E501
        :rtype: dict(str, InvestigationPlaybookTask)
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this InvestigationPlaybook.


        :param tasks: The tasks of this InvestigationPlaybook.  # noqa: E501
        :type: dict(str, InvestigationPlaybookTask)
        """

        self._tasks = tasks

    @property
    def version(self):
        """Gets the version of this InvestigationPlaybook.  # noqa: E501


        :return: The version of this InvestigationPlaybook.  # noqa: E501
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InvestigationPlaybook.


        :param version: The version of this InvestigationPlaybook.  # noqa: E501
        :type: int
        """

        self._version = version

    @property
    def view(self):
        """Gets the view of this InvestigationPlaybook.  # noqa: E501


        :return: The view of this InvestigationPlaybook.  # noqa: E501
        :rtype: PlaybookView
        """
        return self._view

    @view.setter
    def view(self, view):
        """Sets the view of this InvestigationPlaybook.


        :param view: The view of this InvestigationPlaybook.  # noqa: E501
        :type: PlaybookView
        """

        self._view = view

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
        if issubclass(InvestigationPlaybook, dict):
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
        if not isinstance(other, InvestigationPlaybook):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
