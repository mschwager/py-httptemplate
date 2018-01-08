import os

import aiohttp
import aiohttp_jinja2
import jinja2

from . import routes


def get_application(static=False):
    source_directory = os.path.dirname(os.path.dirname(__file__))
    templates_directory = os.path.join(source_directory, 'templates')

    app = aiohttp.web.Application()
    loader = jinja2.FileSystemLoader(templates_directory)

    routes.setup_routes(app)
    aiohttp_jinja2.setup(
        app,
        loader=loader,
        undefined=jinja2.StrictUndefined,
        autoescape=jinja2.select_autoescape()
    )

    if static:
        static_directory = os.path.join(source_directory, 'static')
        app.router.add_static('/static/', path=static_directory, name='static')

    return app
