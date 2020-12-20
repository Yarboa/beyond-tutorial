# import pytest


def test_with_authenticated_client(client, django_user_model):
    username = "admin"
    password = "123456"
    django_user_model.objects.create_user(username=username, password=password)
    # Use this:
    # client.login(username=username, password=password)
    response = client.get('/')
    assert response.status_code == 302
    response = client.get(response.url)
    assert response.status_code == 200
    response = client.get('/accounts/logout')
    assert response.status_code == 301
