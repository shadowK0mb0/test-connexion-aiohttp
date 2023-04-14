import connexion
from connexion.resolver import RelativeResolver

def create_app():
    app = connexion.AioHttpApp(__name__)
    app.add_api('openapi.yaml', resolver=RelativeResolver('app.api'))
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=8000)
