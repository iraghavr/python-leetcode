# coding: utf-8

"""
    Simple Inventory API

    This is a simple API  # noqa: E501

    OpenAPI spec version: 1.0.0-oas3
    Contact: pv.safronov@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BaseSubmissionResult(object):
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
        'code_output': 'list[str]',
        'elapsed_time': 'int',
        'full_runtime_error': 'str',
        'lang': 'str',
        'memory': 'int',
        'memory_percentile': 'float',
        'pretty_lang': 'str',
        'run_success': 'bool',
        'runtime_error': 'str',
        'runtime_percentile': 'float',
        'state': 'str',
        'status_code': 'int',
        'status_memory': 'str',
        'status_msg': 'str',
        'status_runtime': 'str',
        'submission_id': 'str',
        'task_finish_time': 'int',
        'total_correct': 'int',
        'total_testcases': 'int',
        'question_id': 'int'
    }

    attribute_map = {
        'code_output': 'code_output',
        'elapsed_time': 'elapsed_time',
        'full_runtime_error': 'full_runtime_error',
        'lang': 'lang',
        'memory': 'memory',
        'memory_percentile': 'memory_percentile',
        'pretty_lang': 'pretty_lang',
        'run_success': 'run_success',
        'runtime_error': 'runtime_error',
        'runtime_percentile': 'runtime_percentile',
        'state': 'state',
        'status_code': 'status_code',
        'status_memory': 'status_memory',
        'status_msg': 'status_msg',
        'status_runtime': 'status_runtime',
        'submission_id': 'submission_id',
        'task_finish_time': 'task_finish_time',
        'total_correct': 'total_correct',
        'total_testcases': 'total_testcases',
        'question_id': 'question_id'
    }

    def __init__(self, code_output=None, elapsed_time=None, full_runtime_error=None, lang=None, memory=None, memory_percentile=None, pretty_lang=None, run_success=None, runtime_error=None, runtime_percentile=None, state=None, status_code=None, status_memory=None, status_msg=None, status_runtime=None, submission_id=None, task_finish_time=None, total_correct=None, total_testcases=None, question_id=None):  # noqa: E501
        """BaseSubmissionResult - a model defined in Swagger"""  # noqa: E501
        self._code_output = None
        self._elapsed_time = None
        self._full_runtime_error = None
        self._lang = None
        self._memory = None
        self._memory_percentile = None
        self._pretty_lang = None
        self._run_success = None
        self._runtime_error = None
        self._runtime_percentile = None
        self._state = None
        self._status_code = None
        self._status_memory = None
        self._status_msg = None
        self._status_runtime = None
        self._submission_id = None
        self._task_finish_time = None
        self._total_correct = None
        self._total_testcases = None
        self._question_id = None
        self.discriminator = None
        if code_output is not None:
            self.code_output = code_output
        self.elapsed_time = elapsed_time
        if full_runtime_error is not None:
            self.full_runtime_error = full_runtime_error
        self.lang = lang
        self.memory = memory
        if memory_percentile is not None:
            self.memory_percentile = memory_percentile
        self.pretty_lang = pretty_lang
        self.run_success = run_success
        if runtime_error is not None:
            self.runtime_error = runtime_error
        if runtime_percentile is not None:
            self.runtime_percentile = runtime_percentile
        self.state = state
        self.status_code = status_code
        if status_memory is not None:
            self.status_memory = status_memory
        self.status_msg = status_msg
        self.status_runtime = status_runtime
        self.submission_id = submission_id
        self.task_finish_time = task_finish_time
        if total_correct is not None:
            self.total_correct = total_correct
        if total_testcases is not None:
            self.total_testcases = total_testcases
        if question_id is not None:
            self.question_id = question_id

    @property
    def code_output(self):
        """Gets the code_output of this BaseSubmissionResult.  # noqa: E501


        :return: The code_output of this BaseSubmissionResult.  # noqa: E501
        :rtype: list[str]
        """
        return self._code_output

    @code_output.setter
    def code_output(self, code_output):
        """Sets the code_output of this BaseSubmissionResult.


        :param code_output: The code_output of this BaseSubmissionResult.  # noqa: E501
        :type: list[str]
        """

        self._code_output = code_output

    @property
    def elapsed_time(self):
        """Gets the elapsed_time of this BaseSubmissionResult.  # noqa: E501


        :return: The elapsed_time of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._elapsed_time

    @elapsed_time.setter
    def elapsed_time(self, elapsed_time):
        """Sets the elapsed_time of this BaseSubmissionResult.


        :param elapsed_time: The elapsed_time of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """
        if elapsed_time is None:
            raise ValueError("Invalid value for `elapsed_time`, must not be `None`")  # noqa: E501

        self._elapsed_time = elapsed_time

    @property
    def full_runtime_error(self):
        """Gets the full_runtime_error of this BaseSubmissionResult.  # noqa: E501


        :return: The full_runtime_error of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._full_runtime_error

    @full_runtime_error.setter
    def full_runtime_error(self, full_runtime_error):
        """Sets the full_runtime_error of this BaseSubmissionResult.


        :param full_runtime_error: The full_runtime_error of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """

        self._full_runtime_error = full_runtime_error

    @property
    def lang(self):
        """Gets the lang of this BaseSubmissionResult.  # noqa: E501


        :return: The lang of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this BaseSubmissionResult.


        :param lang: The lang of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if lang is None:
            raise ValueError("Invalid value for `lang`, must not be `None`")  # noqa: E501

        self._lang = lang

    @property
    def memory(self):
        """Gets the memory of this BaseSubmissionResult.  # noqa: E501


        :return: The memory of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this BaseSubmissionResult.


        :param memory: The memory of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """
        if memory is None:
            raise ValueError("Invalid value for `memory`, must not be `None`")  # noqa: E501

        self._memory = memory

    @property
    def memory_percentile(self):
        """Gets the memory_percentile of this BaseSubmissionResult.  # noqa: E501


        :return: The memory_percentile of this BaseSubmissionResult.  # noqa: E501
        :rtype: float
        """
        return self._memory_percentile

    @memory_percentile.setter
    def memory_percentile(self, memory_percentile):
        """Sets the memory_percentile of this BaseSubmissionResult.


        :param memory_percentile: The memory_percentile of this BaseSubmissionResult.  # noqa: E501
        :type: float
        """

        self._memory_percentile = memory_percentile

    @property
    def pretty_lang(self):
        """Gets the pretty_lang of this BaseSubmissionResult.  # noqa: E501


        :return: The pretty_lang of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._pretty_lang

    @pretty_lang.setter
    def pretty_lang(self, pretty_lang):
        """Sets the pretty_lang of this BaseSubmissionResult.


        :param pretty_lang: The pretty_lang of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if pretty_lang is None:
            raise ValueError("Invalid value for `pretty_lang`, must not be `None`")  # noqa: E501

        self._pretty_lang = pretty_lang

    @property
    def run_success(self):
        """Gets the run_success of this BaseSubmissionResult.  # noqa: E501


        :return: The run_success of this BaseSubmissionResult.  # noqa: E501
        :rtype: bool
        """
        return self._run_success

    @run_success.setter
    def run_success(self, run_success):
        """Sets the run_success of this BaseSubmissionResult.


        :param run_success: The run_success of this BaseSubmissionResult.  # noqa: E501
        :type: bool
        """
        if run_success is None:
            raise ValueError("Invalid value for `run_success`, must not be `None`")  # noqa: E501

        self._run_success = run_success

    @property
    def runtime_error(self):
        """Gets the runtime_error of this BaseSubmissionResult.  # noqa: E501


        :return: The runtime_error of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._runtime_error

    @runtime_error.setter
    def runtime_error(self, runtime_error):
        """Sets the runtime_error of this BaseSubmissionResult.


        :param runtime_error: The runtime_error of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """

        self._runtime_error = runtime_error

    @property
    def runtime_percentile(self):
        """Gets the runtime_percentile of this BaseSubmissionResult.  # noqa: E501


        :return: The runtime_percentile of this BaseSubmissionResult.  # noqa: E501
        :rtype: float
        """
        return self._runtime_percentile

    @runtime_percentile.setter
    def runtime_percentile(self, runtime_percentile):
        """Sets the runtime_percentile of this BaseSubmissionResult.


        :param runtime_percentile: The runtime_percentile of this BaseSubmissionResult.  # noqa: E501
        :type: float
        """

        self._runtime_percentile = runtime_percentile

    @property
    def state(self):
        """Gets the state of this BaseSubmissionResult.  # noqa: E501


        :return: The state of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BaseSubmissionResult.


        :param state: The state of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if state is None:
            raise ValueError("Invalid value for `state`, must not be `None`")  # noqa: E501
        allowed_values = ["SUCCESS"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def status_code(self):
        """Gets the status_code of this BaseSubmissionResult.  # noqa: E501


        :return: The status_code of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this BaseSubmissionResult.


        :param status_code: The status_code of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """
        if status_code is None:
            raise ValueError("Invalid value for `status_code`, must not be `None`")  # noqa: E501
        allowed_values = [10, 11, 15]  # noqa: E501
        if status_code not in allowed_values:
            raise ValueError(
                "Invalid value for `status_code` ({0}), must be one of {1}"  # noqa: E501
                .format(status_code, allowed_values)
            )

        self._status_code = status_code

    @property
    def status_memory(self):
        """Gets the status_memory of this BaseSubmissionResult.  # noqa: E501


        :return: The status_memory of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._status_memory

    @status_memory.setter
    def status_memory(self, status_memory):
        """Sets the status_memory of this BaseSubmissionResult.


        :param status_memory: The status_memory of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """

        self._status_memory = status_memory

    @property
    def status_msg(self):
        """Gets the status_msg of this BaseSubmissionResult.  # noqa: E501


        :return: The status_msg of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._status_msg

    @status_msg.setter
    def status_msg(self, status_msg):
        """Sets the status_msg of this BaseSubmissionResult.


        :param status_msg: The status_msg of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if status_msg is None:
            raise ValueError("Invalid value for `status_msg`, must not be `None`")  # noqa: E501

        self._status_msg = status_msg

    @property
    def status_runtime(self):
        """Gets the status_runtime of this BaseSubmissionResult.  # noqa: E501


        :return: The status_runtime of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._status_runtime

    @status_runtime.setter
    def status_runtime(self, status_runtime):
        """Sets the status_runtime of this BaseSubmissionResult.


        :param status_runtime: The status_runtime of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if status_runtime is None:
            raise ValueError("Invalid value for `status_runtime`, must not be `None`")  # noqa: E501

        self._status_runtime = status_runtime

    @property
    def submission_id(self):
        """Gets the submission_id of this BaseSubmissionResult.  # noqa: E501


        :return: The submission_id of this BaseSubmissionResult.  # noqa: E501
        :rtype: str
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        """Sets the submission_id of this BaseSubmissionResult.


        :param submission_id: The submission_id of this BaseSubmissionResult.  # noqa: E501
        :type: str
        """
        if submission_id is None:
            raise ValueError("Invalid value for `submission_id`, must not be `None`")  # noqa: E501

        self._submission_id = submission_id

    @property
    def task_finish_time(self):
        """Gets the task_finish_time of this BaseSubmissionResult.  # noqa: E501


        :return: The task_finish_time of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._task_finish_time

    @task_finish_time.setter
    def task_finish_time(self, task_finish_time):
        """Sets the task_finish_time of this BaseSubmissionResult.


        :param task_finish_time: The task_finish_time of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """
        if task_finish_time is None:
            raise ValueError("Invalid value for `task_finish_time`, must not be `None`")  # noqa: E501

        self._task_finish_time = task_finish_time

    @property
    def total_correct(self):
        """Gets the total_correct of this BaseSubmissionResult.  # noqa: E501


        :return: The total_correct of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._total_correct

    @total_correct.setter
    def total_correct(self, total_correct):
        """Sets the total_correct of this BaseSubmissionResult.


        :param total_correct: The total_correct of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """

        self._total_correct = total_correct

    @property
    def total_testcases(self):
        """Gets the total_testcases of this BaseSubmissionResult.  # noqa: E501


        :return: The total_testcases of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._total_testcases

    @total_testcases.setter
    def total_testcases(self, total_testcases):
        """Sets the total_testcases of this BaseSubmissionResult.


        :param total_testcases: The total_testcases of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """

        self._total_testcases = total_testcases

    @property
    def question_id(self):
        """Gets the question_id of this BaseSubmissionResult.  # noqa: E501


        :return: The question_id of this BaseSubmissionResult.  # noqa: E501
        :rtype: int
        """
        return self._question_id

    @question_id.setter
    def question_id(self, question_id):
        """Sets the question_id of this BaseSubmissionResult.


        :param question_id: The question_id of this BaseSubmissionResult.  # noqa: E501
        :type: int
        """

        self._question_id = question_id

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
        if issubclass(BaseSubmissionResult, dict):
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
        if not isinstance(other, BaseSubmissionResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
