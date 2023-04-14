import pytest

from app.main import create_app

@pytest.mark.asyncio
async def test_get(aiohttp_client):
    app = create_app()
    client = await aiohttp_client(app.app)
    response = await client.post('/myapi/reverse', json={'string': 'hello'})
    print(response)
    assert response.status == 200
    assert await response.text() == '{"string": "olleh"}\n'