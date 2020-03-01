# coding: utf-8

"""
    configapi

    Config API lets you easily manage configuration at scale.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class HttpOrchestrationResponse(object):
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
        'successful': 'bool',
        'tasks_completed': 'int',
        'output_string_type': 'str',
        'output_binary_type': 'str'
    }

    attribute_map = {
        'successful': 'Successful',
        'tasks_completed': 'TasksCompleted',
        'output_string_type': 'Output_StringType',
        'output_binary_type': 'Output_BinaryType'
    }

    def __init__(self, successful=None, tasks_completed=None, output_string_type=None, output_binary_type=None):  # noqa: E501
        """HttpOrchestrationResponse - a model defined in Swagger"""  # noqa: E501

        self._successful = None
        self._tasks_completed = None
        self._output_string_type = None
        self._output_binary_type = None
        self.discriminator = None

        if successful is not None:
            self.successful = successful
        if tasks_completed is not None:
            self.tasks_completed = tasks_completed
        if output_string_type is not None:
            self.output_string_type = output_string_type
        if output_binary_type is not None:
            self.output_binary_type = output_binary_type

    @property
    def successful(self):
        """Gets the successful of this HttpOrchestrationResponse.  # noqa: E501

        True if the operation was successful, false otherwise  # noqa: E501

        :return: The successful of this HttpOrchestrationResponse.  # noqa: E501
        :rtype: bool
        """
        return self._successful

    @successful.setter
    def successful(self, successful):
        """Sets the successful of this HttpOrchestrationResponse.

        True if the operation was successful, false otherwise  # noqa: E501

        :param successful: The successful of this HttpOrchestrationResponse.  # noqa: E501
        :type: bool
        """

        self._successful = successful

    @property
    def tasks_completed(self):
        """Gets the tasks_completed of this HttpOrchestrationResponse.  # noqa: E501

        Count of the number of tasks that were completed  # noqa: E501

        :return: The tasks_completed of this HttpOrchestrationResponse.  # noqa: E501
        :rtype: int
        """
        return self._tasks_completed

    @tasks_completed.setter
    def tasks_completed(self, tasks_completed):
        """Sets the tasks_completed of this HttpOrchestrationResponse.

        Count of the number of tasks that were completed  # noqa: E501

        :param tasks_completed: The tasks_completed of this HttpOrchestrationResponse.  # noqa: E501
        :type: int
        """

        self._tasks_completed = tasks_completed

    @property
    def output_string_type(self):
        """Gets the output_string_type of this HttpOrchestrationResponse.  # noqa: E501

        Result output in string format  # noqa: E501

        :return: The output_string_type of this HttpOrchestrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._output_string_type

    @output_string_type.setter
    def output_string_type(self, output_string_type):
        """Sets the output_string_type of this HttpOrchestrationResponse.

        Result output in string format  # noqa: E501

        :param output_string_type: The output_string_type of this HttpOrchestrationResponse.  # noqa: E501
        :type: str
        """

        self._output_string_type = output_string_type

    @property
    def output_binary_type(self):
        """Gets the output_binary_type of this HttpOrchestrationResponse.  # noqa: E501

        Result output in binary format  # noqa: E501

        :return: The output_binary_type of this HttpOrchestrationResponse.  # noqa: E501
        :rtype: str
        """
        return self._output_binary_type

    @output_binary_type.setter
    def output_binary_type(self, output_binary_type):
        """Sets the output_binary_type of this HttpOrchestrationResponse.

        Result output in binary format  # noqa: E501

        :param output_binary_type: The output_binary_type of this HttpOrchestrationResponse.  # noqa: E501
        :type: str
        """
        if output_binary_type is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', output_binary_type):  # noqa: E501
            raise ValueError(r"Invalid value for `output_binary_type`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._output_binary_type = output_binary_type

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
        if issubclass(HttpOrchestrationResponse, dict):
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
        if not isinstance(other, HttpOrchestrationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
