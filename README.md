# Testing a Connexion AioHttpApp with pytest

This is a simple example of how to test a Connexion AioHttpApp with pytest.

## Run Locally

To start the application locally, run the following commands:

```bash
pip install -r requirements.txt
python -m app.main
```

The application will start on port 8000. You can access the Swagger UI at http://localhost:8000/myapi/ui.

To curl the API, run the following command:

```bash
curl http://localhost:8000/myapi/reverse -H 'Content-Type: application/json' -d '{"string": "hello world"}'
```
 or via Powershell:

```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:8000/myapi/reverse -Body '{"string": "hello world"}' -ContentType 'application/json'
```

## Run Tests Locally

To run the tests, run the following command:

```bash
python -m pytest
```

## Running via Docker
To run the application or tests via docker run either `make dockerrun` or `make test`. If you do not have access 
to `make` you can run the commands directly in the make file targets, just remember to replace `$(IMAGE_NAME)`

