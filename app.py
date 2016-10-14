#!/usr/bin/env python3
import connexion
from flaskrun import flaskrun

if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.add_api(
        'swagger.yaml',
        arguments={'title': 'Create a map on the top of OpenStreetMap tiles'}
    )
    flaskrun(app)
