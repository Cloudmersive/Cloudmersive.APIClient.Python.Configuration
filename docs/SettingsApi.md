# cloudmersive_configuration_api_client.SettingsApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**settings_create_setting**](SettingsApi.md#settings_create_setting) | **POST** /config/settings/create | Create a setting in the specified bucket
[**settings_list_settings**](SettingsApi.md#settings_list_settings) | **POST** /config/settings/list | Enumerate the settings in a bucket
[**settings_update_setting**](SettingsApi.md#settings_update_setting) | **POST** /config/settings/update | Update a setting


# **settings_create_setting**
> CreateSettingResponse settings_create_setting(request)

Create a setting in the specified bucket

### Example
```python
from __future__ import print_function
import time
import cloudmersive_configuration_api_client
from cloudmersive_configuration_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_configuration_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_configuration_api_client.SettingsApi(cloudmersive_configuration_api_client.ApiClient(configuration))
request = cloudmersive_configuration_api_client.CreateSettingRequest() # CreateSettingRequest | Request to perform the operation on

try:
    # Create a setting in the specified bucket
    api_response = api_instance.settings_create_setting(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_create_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**CreateSettingRequest**](CreateSettingRequest.md)| Request to perform the operation on | 

### Return type

[**CreateSettingResponse**](CreateSettingResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_list_settings**
> ListSettingsResponse settings_list_settings(request)

Enumerate the settings in a bucket

### Example
```python
from __future__ import print_function
import time
import cloudmersive_configuration_api_client
from cloudmersive_configuration_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_configuration_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_configuration_api_client.SettingsApi(cloudmersive_configuration_api_client.ApiClient(configuration))
request = cloudmersive_configuration_api_client.ListSettingsRequest() # ListSettingsRequest | Request to perform the operation on

try:
    # Enumerate the settings in a bucket
    api_response = api_instance.settings_list_settings(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_list_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ListSettingsRequest**](ListSettingsRequest.md)| Request to perform the operation on | 

### Return type

[**ListSettingsResponse**](ListSettingsResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **settings_update_setting**
> UpdateSettingResponse settings_update_setting(request)

Update a setting

### Example
```python
from __future__ import print_function
import time
import cloudmersive_configuration_api_client
from cloudmersive_configuration_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_configuration_api_client.Configuration()
configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Apikey'] = 'Bearer'

# create an instance of the API class
api_instance = cloudmersive_configuration_api_client.SettingsApi(cloudmersive_configuration_api_client.ApiClient(configuration))
request = cloudmersive_configuration_api_client.UpdateSettingRequest() # UpdateSettingRequest | Request to perform the operation on

try:
    # Update a setting
    api_response = api_instance.settings_update_setting(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SettingsApi->settings_update_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdateSettingRequest**](UpdateSettingRequest.md)| Request to perform the operation on | 

### Return type

[**UpdateSettingResponse**](UpdateSettingResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

