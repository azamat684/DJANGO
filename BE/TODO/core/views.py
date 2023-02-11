from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,HttpRequest,HttpResponseBadRequest,HttpResponseRedirect
from django.template import loader

def index(request):
    template = loader.get_template('core/index.html')
    return HttpResponse(template.render())

def about(request):
    return HttpResponse("<h1>Siz about qismidasiz</h1>")