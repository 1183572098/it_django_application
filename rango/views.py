from django.http import HttpResponse


def about(request):
    response = HttpResponse()
    response.write("Rango says here is the about page.")
    response.write("<a href='/rango/'>Index</a>")
    return response


def index(request):
    response = HttpResponse()
    response.write("Rango says hey there partner!")
    response.write("<a href='/rango/about/'>About</a>")
    return response
