from sanic import Sanic

app = Sanic(__name__)
app.static('/assets', './static')