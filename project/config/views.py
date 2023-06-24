from django.http import HttpResponse
from django.template import Context, Template


def hermanos(request):
    mi_html = open("./templates/template1.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def hermanos(request):
    mi_html = open("./templates/template2.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def hermano(request):
    return  HttpResponse("<h1>hola soy hermanos<h1>")