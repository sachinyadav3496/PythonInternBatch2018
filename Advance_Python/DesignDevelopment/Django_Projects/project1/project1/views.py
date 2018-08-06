from django.http import HttpResponse

def index(request):
    page = """<h1 style='color:red'>Welcome to my first Django Page</h1>
    <a href=''>HOME</a>
    <a href='app1/'>APP1</a>
    <a href='app2/'>APP2</a>"""
    return  HttpResponse(page)
