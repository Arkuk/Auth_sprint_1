import pytest
import http


@pytest.mark.asyncio
async def test_get_roles(make_request):
    '''получение списка ролей'''
    response = await make_request(
        endpoint="/api/v1/roles", http_method="get"
    )
    assert response.status == http.HTTPStatus.OK

@pytest.mark.asyncio
async def test_add_role():
    '''добавление новой роли'''
    pass


@pytest.mark.asyncio
async def test_change_role():
    '''корректность изменения имени роли'''
    pass


@pytest.mark.asyncio
async def test_delete_role():
    '''удаление роли'''
    pass

@pytest.mark.asyncio
async def test_no_access():
    '''на любом методе проверяем корректность проверки прав'''
    pass

'''
@pytest.mark.asyncio
async def test_get_by_good_id(create_fake_films, es_check_or_create_index, write_data_in_es, make_get_request):
    await es_check_or_create_index(test_settings.es_index_film)
    data = await create_fake_films(1)
    write_data_in_es(data, test_settings.es_index_film)
    response = await make_get_request(f'films/{data[0].id}')
    assert response['status'] == 200
    assert response['body']['id'] == str(data[0].id)


@pytest.mark.asyncio
async def test_get_by_bad_id(make_get_request):
    response = await make_get_request('films/bad_id')
    assert response['status'] == 404
'''