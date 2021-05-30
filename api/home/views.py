from templates import templates

def home(request):
    return templates.render('home/index.html', request)