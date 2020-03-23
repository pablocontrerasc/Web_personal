from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Aserca de</a></li>
    <li><a href="/portafolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return HttpResponse(html_base +"<h1>Aceerca de</h1>")

def portafolio(request):
    return HttpResponse(html_base +"<h1>esta es el portafolio</h1>")

def contact(request):
    return HttpResponse(html_base +"<h1>esta es el contacto</h1>")
