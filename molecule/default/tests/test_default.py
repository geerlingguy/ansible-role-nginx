"""Role testing files using testinfra."""
import pytest
import requests

def test_is_postgresql_runnnig_and_enabled(host):
    nginx = host.service('nginx')

    assert nginx.is_running
    assert nginx.is_enabled

@pytest.mark.parametrize('path,content', (
('static/static.html', b'static'),
('static/cache.js', b'static'),
('static/cache.css', b'static'),
('media/media.html', b'media')
))
def test_statics_location_is_accessible(host, path, content):
    response = requests.get(f'https://localhost:8080/{path}',
     verify=False)
    response.raise_for_status()
    print(response.headers)
    assert response.content == content

@pytest.mark.parametrize('path,expiry', (
('static/cache.js', 365*24*3600),
('static/cache.css', 365*24*3600),
))
def test_js_and_css_files_are_cached(host, path, expiry):
    response = requests.get(f'https://localhost:8080/{path}', verify=False)
    assert f'max-age={expiry}' in response.headers['Cache-Control']

def test_upstream_is_accessible(host):
    expected = b"Directory listing for /"
    response = requests.get(f'https://localhost:8080/', verify=False)
    assert expected in response.content
