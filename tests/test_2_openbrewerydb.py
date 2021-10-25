import pytest


# Пивоварня по имени и штату
@pytest.mark.parametrize('name, state, brewery_id', [
    ('cooper', 'Massachusetts', ['3cross-fermentation-cooperative-worcester']),
    ('cvdbdr', '', []),
    ('modern', 'Missouri', ['modern-brewery-saint-louis'])])
def test_get_by_name_by_state(api_client, name, state, brewery_id):
    response = api_client.get(f"/breweries/?by_name={name}&by_state={state}").json()
    i = 0
    breweries_id = []
    for response[i] in response:
        for key, value in response[i].items():
            if key == 'id':
                breweries_id.append(response[i].get(key))
    assert breweries_id == brewery_id


# Пивоварня по id
@pytest.mark.parametrize('brewery_id, name, phone', [
    ('bookhouse-brewing-llc-cleveland', 'Bookhouse Brewing, LLC.', '4144264555'),
    ('breaking-point-brewery-cleveland-heights', 'Breaking Point Brewery', '2162357411')])
def test_get_by_id(api_client, brewery_id, name, phone):
    response = api_client.get(f"/breweries/{brewery_id}").json()
    assert response['name'] == name
    assert response['phone'] == phone


# Поиск пивоварни
@pytest.mark.parametrize('search, name, street', [
    ('Band of Brothers', 'Band of Brothers Brewing Company', '1605 23rd Ave')])
def test_get_search(api_client, search, name, street):
    response = api_client.get(f"/breweries/search/?query={search}").json()
    response = response[0]
    assert response['name'] == name
    assert response['street'] == street


# Пивоварня по типу и городу
@pytest.mark.parametrize('brewery_type, city, postal_code', [
    ('planning', 'Cleveland', ['44113-3104', '44115-1111', '30528-7804']),
    ('54564', 'Cleveland', [])])
def test_get_by_type_by_city(api_client, brewery_type, city, postal_code):
    response = api_client.get(f"/breweries/?by_type={brewery_type}&by_city={city}").json()
    i = 0
    breweries_postal_code = []
    for response[i] in response:
        for key, value in response[i].items():
            if key == 'postal_code':
                breweries_postal_code.append(response[i].get(key))
    assert breweries_postal_code == postal_code


# Пивоварня по тегу
@pytest.mark.parametrize('tag, name, brewery_type, street, city, phone', [
    ('patio', '10-56 Brewing Company', 'micro', '400 Brown Cir', 'Knox', '6308165790')])
def test_get_by_tag(api_client, tag, name, brewery_type, street, city, phone):
    response = api_client.get(f"/breweries/?by_tag={tag}").json()
    response = response[0]
    assert response['name'] == name
    assert response['brewery_type'] == brewery_type
    assert response['street'] == street
    assert response['city'] == city
    assert response['phone'] == phone
