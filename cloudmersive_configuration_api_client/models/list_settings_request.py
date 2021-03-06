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


class ListSettingsRequest(object):
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
        'bucket_secret_key': 'str'
    }

    attribute_map = {
        'bucket_id': 'BucketID',
        'bucket_secret_key': 'BucketSecretKey'
    }

    def __init__(self, bucket_id=None, bucket_secret_key=None):  # noqa: E501
        """ListSettingsRequest - a model defined in Swagger"""  # noqa: E501

        self._bucket_id = None
        self._bucket_secret_key = None
        self.discriminator = None

        if bucket_id is not None:
            self.bucket_id = bucket_id
        if bucket_secret_key is not None:
            self.bucket_secret_key = bucket_secret_key

    @property
    def bucket_id(self):
        """Gets the bucket_id of this ListSettingsRequest.  # noqa: E501

        BucketID of the bucket to enumerate the settings of; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :return: The bucket_id of this ListSettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_id

    @bucket_id.setter
    def bucket_id(self, bucket_id):
        """Sets the bucket_id of this ListSettingsRequest.

        BucketID of the bucket to enumerate the settings of; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :param bucket_id: The bucket_id of this ListSettingsRequest.  # noqa: E501
        :type: str
        """

        self._bucket_id = bucket_id

    @property
    def bucket_secret_key(self):
        """Gets the bucket_secret_key of this ListSettingsRequest.  # noqa: E501

        SecretKey of the bucket enumerate the settings of; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :return: The bucket_secret_key of this ListSettingsRequest.  # noqa: E501
        :rtype: str
        """
        return self._bucket_secret_key

    @bucket_secret_key.setter
    def bucket_secret_key(self, bucket_secret_key):
        """Sets the bucket_secret_key of this ListSettingsRequest.

        SecretKey of the bucket enumerate the settings of; you can create a bucket by navigating to account.cloudmersive.com, clicking on Settings &gt; API Configuration &gt; Create Bucket  # noqa: E501

        :param bucket_secret_key: The bucket_secret_key of this ListSettingsRequest.  # noqa: E501
        :type: str
        """

        self._bucket_secret_key = bucket_secret_key

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
        if issubclass(ListSettingsRequest, dict):
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
        if not isinstance(other, ListSettingsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
