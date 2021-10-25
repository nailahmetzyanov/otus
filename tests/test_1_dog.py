import pytest


# Получение фото случайной собаки
def test_get_random_dog(api_client):
    response = api_client.get("breeds/image/random")
    assert response.status_code == 200, f"Неверный код ответа, получен {response.status_code}"
    response = response.json()
    assert response["status"] == "success"


# Список всех фото собак списком содержит только изображения
@pytest.mark.parametrize("file", ['.md', '.MD', '.exe', '.txt'])
def test_get_breed_images(api_client, file):
    response = api_client.get("breed/hound/images")
    response = response.json()
    result = '\n'.join(response["message"])
    assert file not in result, f"В сообщении есть файл с расширением {file}"


# Список фото определенных пород
@pytest.mark.parametrize("breed", [
    "african",
    "boxer",
    "entlebucher",
    "elkhound",
    "shiba",
    "whippet",
    "spaniel"
])
def test_get_random_breed_images(api_client, breed):
    response = api_client.get(f"breed/{breed}/images/")
    response = response.json()
    assert response["status"] == "success", f"Не удалось получить список изображений породы {breed}"


# Список определенного количества случайных фото
@pytest.mark.parametrize("number_of_images", [i for i in range(1, 10)])
def test_get_few_sub_breed_random_images(api_client, number_of_images):
    response = api_client.get(f"breed/hound/afghan/images/random/{number_of_images}")
    response = response.json()
    final_len = len(response["message"])
    assert final_len == number_of_images, f"Количество фото не {number_of_images}, а {final_len}"


# Фото случайной собаки из определенной породы
@pytest.mark.parametrize("breed", [
    "afghan",
    "basset",
    "blood",
    "english",
    "ibizan",
    "plott",
    "walker"
])
def test_get_random_breed_image(api_client, breed):
    response = api_client.get(f"breed/{breed}/images/random")
    response = response.json()
    assert breed not in response["message"], f"Нет ссылки на фото с указанной породой, ответ {response}"
