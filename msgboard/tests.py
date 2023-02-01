# import pytest


def test_posts_with_client(client, django_user_model):
    # Use this:
    response = client.get('/posts/')
    assert response.status_code == 200
    assert isinstance(response.context['blog_list'], list)
    template_names = set(tmpl.origin.template_name for tmpl in response.templates)
    assert 'msgboard/post_list.html' in template_names
