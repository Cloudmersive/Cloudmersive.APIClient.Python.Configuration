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


class TaskOutputReference(object):
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
        'task_name': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'task_name': 'TaskName',
        'target_type': 'TargetType'
    }

    def __init__(self, task_name=None, target_type=None):  # noqa: E501
        """TaskOutputReference - a model defined in Swagger"""  # noqa: E501

        self._task_name = None
        self._target_type = None
        self.discriminator = None

        if task_name is not None:
            self.task_name = task_name
        if target_type is not None:
            self.target_type = target_type

    @property
    def task_name(self):
        """Gets the task_name of this TaskOutputReference.  # noqa: E501

        Name of the task to use the output from  # noqa: E501

        :return: The task_name of this TaskOutputReference.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this TaskOutputReference.

        Name of the task to use the output from  # noqa: E501

        :param task_name: The task_name of this TaskOutputReference.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def target_type(self):
        """Gets the target_type of this TaskOutputReference.  # noqa: E501

        Type to convert the output from the referenced task to; possible values are string, binary  # noqa: E501

        :return: The target_type of this TaskOutputReference.  # noqa: E501
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """Sets the target_type of this TaskOutputReference.

        Type to convert the output from the referenced task to; possible values are string, binary  # noqa: E501

        :param target_type: The target_type of this TaskOutputReference.  # noqa: E501
        :type: str
        """

        self._target_type = target_type

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
        if issubclass(TaskOutputReference, dict):
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
        if not isinstance(other, TaskOutputReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other