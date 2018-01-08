from . import views


def setup_routes(app):
    app.router.add_get('/', views.index)
    app.router.add_get('/about', views.about)
