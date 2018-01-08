import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'content_header': 'Content Header'}


@aiohttp_jinja2.template('about.html')
async def about(request):
    return {}
