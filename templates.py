from sanic import Sanic
from sanic_jinja2 import SanicJinja2

from filters import (
    date
)

app = Sanic.get_app()

templates = SanicJinja2(app, pkg_name='resources')
templates.env.filters['date'] = date