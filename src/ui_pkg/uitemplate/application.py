import pkg_resources

import aiohttp
import aiohttp_jinja2
import jinja2

from . import routes
from . import about


def get_application(static=False):
    templates_directory = pkg_resources.resource_filename(about.__name__, 'templates')
    static_directory = pkg_resources.resource_filename(about.__name__, 'static')

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
        app.router.add_static('/static/', path=static_directory)

    return app
