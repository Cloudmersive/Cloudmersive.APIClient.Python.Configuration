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


class HttpFormDataParameter(object):
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
        'parameter_name': 'str',
        'parameter_text_value': 'str',
        'parameter_file_contents': 'str',
        'use_output_from_previous_task': 'TaskOutputReference'
    }

    attribute_map = {
        'parameter_name': 'ParameterName',
        'parameter_text_value': 'ParameterTextValue',
        'parameter_file_contents': 'ParameterFileContents',
        'use_output_from_previous_task': 'UseOutputFromPreviousTask'
    }

    def __init__(self, parameter_name=None, parameter_text_value=None, parameter_file_contents=None, use_output_from_previous_task=None):  # noqa: E501
        """HttpFormDataParameter - a model defined in Swagger"""  # noqa: E501

        self._parameter_name = None
        self._parameter_text_value = None
        self._parameter_file_contents = None
        self._use_output_from_previous_task = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_text_value is not None:
            self.parameter_text_value = parameter_text_value
        if parameter_file_contents is not None:
            self.parameter_file_contents = parameter_file_contents
        if use_output_from_previous_task is not None:
            self.use_output_from_previous_task = use_output_from_previous_task

    @property
    def parameter_name(self):
        """Gets the parameter_name of this HttpFormDataParameter.  # noqa: E501

        Name of the parameter  # noqa: E501

        :return: The parameter_name of this HttpFormDataParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this HttpFormDataParameter.

        Name of the parameter  # noqa: E501

        :param parameter_name: The parameter_name of this HttpFormDataParameter.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def parameter_text_value(self):
        """Gets the parameter_text_value of this HttpFormDataParameter.  # noqa: E501

        Text value of the parameter; if set, do not set ParameterFileContents or UseOutputFromPreviousTask  # noqa: E501

        :return: The parameter_text_value of this HttpFormDataParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_text_value

    @parameter_text_value.setter
    def parameter_text_value(self, parameter_text_value):
        """Sets the parameter_text_value of this HttpFormDataParameter.

        Text value of the parameter; if set, do not set ParameterFileContents or UseOutputFromPreviousTask  # noqa: E501

        :param parameter_text_value: The parameter_text_value of this HttpFormDataParameter.  # noqa: E501
        :type: str
        """

        self._parameter_text_value = parameter_text_value

    @property
    def parameter_file_contents(self):
        """Gets the parameter_file_contents of this HttpFormDataParameter.  # noqa: E501

        Binary contents of the parameter; if set, do not set ParameterTextValue or UseOutputFromPreviousTask  # noqa: E501

        :return: The parameter_file_contents of this HttpFormDataParameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_file_contents

    @parameter_file_contents.setter
    def parameter_file_contents(self, parameter_file_contents):
        """Sets the parameter_file_contents of this HttpFormDataParameter.

        Binary contents of the parameter; if set, do not set ParameterTextValue or UseOutputFromPreviousTask  # noqa: E501

        :param parameter_file_contents: The parameter_file_contents of this HttpFormDataParameter.  # noqa: E501
        :type: str
        """
        if parameter_file_contents is not None and not re.search(r'^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$', parameter_file_contents):  # noqa: E501
            raise ValueError(r"Invalid value for `parameter_file_contents`, must be a follow pattern or equal to `/^(?:[A-Za-z0-9+\/]{4})*(?:[A-Za-z0-9+\/]{2}==|[A-Za-z0-9+\/]{3}=)?$/`")  # noqa: E501

        self._parameter_file_contents = parameter_file_contents

    @property
    def use_output_from_previous_task(self):
        """Gets the use_output_from_previous_task of this HttpFormDataParameter.  # noqa: E501

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :return: The use_output_from_previous_task of this HttpFormDataParameter.  # noqa: E501
        :rtype: TaskOutputReference
        """
        return self._use_output_from_previous_task

    @use_output_from_previous_task.setter
    def use_output_from_previous_task(self, use_output_from_previous_task):
        """Sets the use_output_from_previous_task of this HttpFormDataParameter.

        Optional; use the output from a previous task as the input to this parameter.  Set to null (default) to ignore.  # noqa: E501

        :param use_output_from_previous_task: The use_output_from_previous_task of this HttpFormDataParameter.  # noqa: E501
        :type: TaskOutputReference
        """

        self._use_output_from_previous_task = use_output_from_previous_task

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
        if issubclass(HttpFormDataParameter, dict):
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
        if not isinstance(other, HttpFormDataParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
