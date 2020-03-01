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


class CreateSettingRequest(object):
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
        'bucket_id': 'str',
        'bucket_secret_key': 'str',
        'setting_name': 'str',
        'setting_type': 'str',
        'setting_value': 'object',
        'setting_description': 'str',
        'setting_tags': 'str'
    }

    attribute_map = {
        'bucket_id': 'BucketID',
        'bucket_secret_key': 'BucketSecretKey',
        'setting_name': 'SettingName',
        'setting_type': 'SettingType',
        'setting_value': 'SettingValue',
        'setting_description': 'SettingDescription',
        'setting_tags': 'SettingTags'
    }

    def __init__(self, bucket_id=None, bucket_secret_key=None, setting_name=None, setting_type=None, setting_value=None, setting_description=None, setting_tags=None):  # noqa: E501
        """CreateSettingRequest - a model defined in Swagger"""  # noqa: E501

        self._bucket_id = None
        self._bucket_secret_key = None
        self._setting_name = None
        self._setting_type = None
        self._setting_value = None
        self._setting_description = None
        self._setting_tags = None
        self.discriminator = None

        if bucket_id is not None:
            self.bucket_id = bucket_id
        if bucket_secret_key is not None:
            self.bucket_secret_key = bucket_secret_key
        if setting_name is not None:
            self.setting_name = setting_name
        if setting_type is not None:
            self.setting_type = setting_type
        if setting_value is not None:
            self.setting_value = setting_value
        if setting_description is not None:
            self.setting_description = setting_description
        if setting_tags is not None:
            self.setting_tags = setting_tags

    @property
    def bucket_id(self):
        """Gets the bucket_id of this CreateSettingRequest.  # noqa: E501

        BucketID of the bucket to place the setting in; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :return: The bucket_id of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this CreateSettingRequest.

        BucketID of the bucket to place the setting in; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :param bucket_id: The bucket_id of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def bucket_secret_key(self):
        """Gets the bucket_secret_key of this CreateSettingRequest.  # noqa: E501

        SecretKey of the bucket to place the setting in; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :return: The bucket_secret_key of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_secret_key

    @bucket_secret_key.setter
    def bucket_secret_key(self, bucket_secret_key):
        """Sets the bucket_secret_key of this CreateSettingRequest.

        SecretKey of the bucket to place the setting in; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :param bucket_secret_key: The bucket_secret_key of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._bucket_secret_key = bucket_secret_key

    @property
    def setting_name(self):
        """Gets the setting_name of this CreateSettingRequest.  # noqa: E501

        Name of the setting to create  # noqa: E501

        :return: The setting_name of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._setting_name

    @setting_name.setter
    def setting_name(self, setting_name):
        """Sets the setting_name of this CreateSettingRequest.

        Name of the setting to create  # noqa: E501

        :param setting_name: The setting_name of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._setting_name = setting_name

    @property
    def setting_type(self):
        """Gets the setting_type of this CreateSettingRequest.  # noqa: E501

        Type of setting to create; possible values are STRING, JSON  # noqa: E501

        :return: The setting_type of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._setting_type

    @setting_type.setter
    def setting_type(self, setting_type):
        """Sets the setting_type of this CreateSettingRequest.

        Type of setting to create; possible values are STRING, JSON  # noqa: E501

        :param setting_type: The setting_type of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._setting_type = setting_type

    @property
    def setting_value(self):
        """Gets the setting_value of this CreateSettingRequest.  # noqa: E501

        Initial value of the setting  # noqa: E501

        :return: The setting_value of this CreateSettingRequest.  # noqa: E501
        :rtype: object
        """
        return self._setting_value

    @setting_value.setter
    def setting_value(self, setting_value):
        """Sets the setting_value of this CreateSettingRequest.

        Initial value of the setting  # noqa: E501

        :param setting_value: The setting_value of this CreateSettingRequest.  # noqa: E501
        :type: object
        """

        self._setting_value = setting_value

    @property
    def setting_description(self):
        """Gets the setting_description of this CreateSettingRequest.  # noqa: E501

        Description of the setting  # noqa: E501

        :return: The setting_description of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._setting_description

    @setting_description.setter
    def setting_description(self, setting_description):
        """Sets the setting_description of this CreateSettingRequest.

        Description of the setting  # noqa: E501

        :param setting_description: The setting_description of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._setting_description = setting_description

    @property
    def setting_tags(self):
        """Gets the setting_tags of this CreateSettingRequest.  # noqa: E501

        Tags to apply to the setting  # noqa: E501

        :return: The setting_tags of this CreateSettingRequest.  # noqa: E501
        :rtype: str
        """
        return self._setting_tags

    @setting_tags.setter
    def setting_tags(self, setting_tags):
        """Sets the setting_tags of this CreateSettingRequest.

        Tags to apply to the setting  # noqa: E501

        :param setting_tags: The setting_tags of this CreateSettingRequest.  # noqa: E501
        :type: str
        """

        self._setting_tags = setting_tags

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
        if issubclass(CreateSettingRequest, dict):
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
        if not isinstance(other, CreateSettingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other