"""
These tests cover the basic call for each clusters Login page.
"""
import pytest
import requests
from conftest import clusters

@pytest.mark.parametrize('cluster', clusters)
@pytest.mark.api_tests
def test_api_clusters(cluster):
    response = requests.get(cluster)
    assert response.status_code == 200