from django.http import HttpResponse
from django.shortcuts import render


def about(request):
    # response = HttpResponse()
    # response.write("Rango says here is the about page.")
    # response.write("<a href='/rango/'>Index</a>")
    return render(request, 'rango/about.html')


def index(request):
    # response = HttpResponse()
    # response.write("Rango says hey there partner!")
    # response.write("<a href='/rango/about/'>About</a>")
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)
