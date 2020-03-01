# cloudmersive_configuration_api_client.OrchestratorApi

All URIs are relative to *https://api.cloudmersive.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orchestrator_http_simple**](OrchestratorApi.md#orchestrator_http_simple) | **POST** /config/orchestrator/http/simple | Orchestrate multiple HTTP API calls with a single API call in the order specified.  Call other Cloudmersive APIs or third party APIs.  For Cloudmersive APIs, the API Key will automatically propogate to the child calls without needing to be set explicitly.  Name each task and reference the output of a previous task in the inputs to a given task.


# **orchestrator_http_simple**
> HttpOrchestrationResponse orchestrator_http_simple(request)

Orchestrate multiple HTTP API calls with a single API call in the order specified.  Call other Cloudmersive APIs or third party APIs.  For Cloudmersive APIs, the API Key will automatically propogate to the child calls without needing to be set explicitly.  Name each task and reference the output of a previous task in the inputs to a given task.

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
api_instance = cloudmersive_configuration_api_client.OrchestratorApi(cloudmersive_configuration_api_client.ApiClient(configuration))
request = cloudmersive_configuration_api_client.HttpOrchestrationRequest() # HttpOrchestrationRequest | 

try:
    # Orchestrate multiple HTTP API calls with a single API call in the order specified.  Call other Cloudmersive APIs or third party APIs.  For Cloudmersive APIs, the API Key will automatically propogate to the child calls without needing to be set explicitly.  Name each task and reference the output of a previous task in the inputs to a given task.
    api_response = api_instance.orchestrator_http_simple(request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrchestratorApi->orchestrator_http_simple: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**HttpOrchestrationRequest**](HttpOrchestrationRequest.md)|  | 

### Return type

[**HttpOrchestrationResponse**](HttpOrchestrationResponse.md)

### Authorization

[Apikey](../README.md#Apikey)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

