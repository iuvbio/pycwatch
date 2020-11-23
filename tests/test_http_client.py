import pytest
import requests
import requests_mock

from conftest import log_has
from pycwatch.errors import APIError
from pycwatch.rest import HTTPClient, BaseRequest, PRODUCTION_URL


@pytest.fixture
def http_client():
    client = HTTPClient(None, None)
    return client
    

class MockRequest(BaseRequest):
    params = ['param']

    def __init__(self, part, param):
        self.part = part
        self.param = param

    @property
    def endpoint(self):
        return '/path/{part}'.format(part=self.part)


@pytest.fixture
def mock_request():
    request = MockRequest('test-part', 'test-value')
    return request


def test_client():
    client = HTTPClient(api_key=None, headers=None)
    assert client.headers == client.DEFAULT_HEADERS


def test_client_with_key():
    client = HTTPClient(api_key="test-key", headers=None)
    headers = {**client.DEFAULT_HEADERS, "X-CW-API-Key": "test-key"}
    assert client.headers == headers


def test_client_with_headers():
    test_headers = {'test-header1': 'test-value1',
                    'test-header2': 'test-value2'}
    client = HTTPClient(api_key=None, headers=test_headers)
    headers = {**client.DEFAULT_HEADERS, **test_headers}
    assert client.headers == headers


def test_with_header(http_client):
    test_key, test_value = 'test-key', 'test-value'
    http_client.with_header(test_key, test_value)
    headers = {**http_client.DEFAULT_HEADERS, test_key: test_value}
    assert http_client.headers == headers


def test_with_headers(http_client):
    test_headers = {'test-header1': 'test-value1',
                    'test-header2': 'test-value2'}
    http_client.with_headers(test_headers)
    headers = {**http_client.DEFAULT_HEADERS, **test_headers}
    assert http_client.headers == headers


def test_get_resource(http_client, mock_request):
    base_url = PRODUCTION_URL.format(endpoint="/path/test-part")
    resource_expected = base_url + "?param=test-value"
    resource = http_client.get_resource(mock_request)
    assert resource == resource_expected
 

@requests_mock.Mocker(kw='rmock')
def test_perform_good_response(http_client, mock_request, **kwargs):
    resource = http_client.get_resource(mock_request)
    response_expected = {'a': 2}
    kwargs['rmock'].register_uri('GET', resource, json=response_expected,
                                 status_code=200)
    assert http_client.raw_response is None
    response = http_client.perform(mock_request)
    assert response == response_expected
    assert isinstance(http_client.raw_response, requests.models.Response)


@requests_mock.Mocker(kw='rmock')
def test_perform_bad_response(http_client, mock_request, caplog, **kwargs):
    resource = http_client.get_resource(mock_request)
    response_expected = 'Not Found'
    kwargs['rmock'].register_uri('GET', resource, text=response_expected,
                                 status_code=404)
    assert http_client.raw_response is None
    with pytest.raises(APIError):
        response = http_client.perform(mock_request)
        assert response.text == response_expected
        assert isinstance(http_client.raw_response, requests.models.Response)
        assert log_has(response.text, caplog)