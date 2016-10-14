# coding: utf-8

from io import BytesIO

from staticmap import StaticMap
from flask import send_file


def get_static_map_get(latitude, longitude, height, width, zoom, urltemplate):
    m = StaticMap(width, height, url_template=urltemplate)

    image = m.render(zoom=5, center=(longitude, latitude))

    img_io = BytesIO()
    image.save(img_io, 'png', quality=90)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
