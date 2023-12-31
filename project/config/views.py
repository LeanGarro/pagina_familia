from django.http import HttpResponse
from django.template import Context, Template


def inicio(request):
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

def padres(request):
    mi_html = open("./templates/template3.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)

def abuelos(request):
    mi_html = open("./templates/template4.html")
    mi_template = Template(mi_html.read())
    mi_html.close()
    mi_contexto = Context()
    mi_documento = mi_template.render(mi_contexto)
    return HttpResponse(mi_documento)