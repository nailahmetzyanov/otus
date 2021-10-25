import pytest


# Список пользователей
@pytest.mark.parametrize('output_id', [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])])
def test_get_users(api_client, output_id):
    response = api_client.get(f"/users/").json()
    i = 0
    user_id = []
    for response[i] in response:
        for key, value in response[i].items():
            if key == 'id':
                user_id.append(response[i].get(key))
    assert user_id == output_id


# Cообщение по id
@pytest.mark.parametrize('post_id, output_id, output_user_id, title', [
    ('4', 4, 1, 'eum et est occaecati'),
    ('35', 35, 4, ['id nihil consequatur molestias animi provident'])])
def test_get_posts_id(api_client, post_id, output_id, output_user_id, title):
    response = api_client.get(f"/posts/{post_id}").json()
    assert response['id'] == output_id
    assert response['userId'] == output_user_id
    assert response['title'] == title


# Комментарии к посту по id поста
@pytest.mark.parametrize('input_post_id, output_id, output_name', [
    ('44', [216, 217, 218, 219, 220], ['voluptatem esse sint alias', 'eos velit velit esse autem minima voluptas',
                                       'voluptatem qui deserunt dolorum in voluptates similique et qui',
                                       'qui unde recusandae omnis ut explicabo neque magni veniam',
                                       'vel autem quia in modi velit'])])
def test_get_comments_id(api_client, input_post_id, output_id, output_name):
    response = api_client.get(f"/comments/?postId={input_post_id}").json()
    i = 0
    ids = []
    names = []
    for response[i] in response:
        for key, value in response[i].items():
            if key == 'id':
                ids.append(response[i].get(key))
            if key == 'name':
                names.append(response[i].get(key))
    assert ids == output_id
    assert names == output_name


# Создание нового ресурса по id поста
@pytest.mark.parametrize('input_id, input_title',
                         [(663773, 'this test title')])
@pytest.mark.parametrize('output_id, output_title',
                         [('663773', 'this test title')])
def test_get_create_resource(api_client, input_id, output_id, input_title, output_title):
    response = api_client.post(f"/posts",
                                        data={'title': input_title, 'body': 'bar', 'userId': input_id}).json()
    assert response['title'] == output_title
    assert response['body'] == 'bar'
    assert response['userId'] == output_id


# Все альбомы проверяем кол-во полученных записей
@pytest.mark.parametrize('output_id', [([100])])
def test_get_all_albums(api_client, output_id):
    response = api_client.get(f"/albums").json()
    i = 0
    count = 0
    for response[i] in response:
        for key, value in response[i].items():
            if key == 'id':
                count += 1
    assert count == output_id
