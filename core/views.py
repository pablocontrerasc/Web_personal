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
    return render(request, "core/about.html")

def portafolio(request):
    return render(request, "core/portafolio.html")

def contact(request):
    return render(request, "core/contact.html")
