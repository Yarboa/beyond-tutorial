# from django.test import TestCase

# Create your tests here.

def test_with_client(client):
    response = client.get('/posts/')
    assert response.status_code == 200 
    assert response.context['blog_list'] == ['article1 content1', 'article2 content2'] 
 #    response = client.get(response.url)
#    assert b"article1" in response.content
