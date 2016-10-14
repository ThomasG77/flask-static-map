# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

To run the server, please execute the following:

```

virtualenv venv --python=/usr/bin/python3.5
source venv/bin/activate
pip install -U connexion # install Connexion from PyPI
# You need to install staticmap
pip install https://github.com/komoot/staticmap/archive/master.zip
python app.py
```


and open your browser to here:

```
http://localhost:8080/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v1/swagger.json
```

