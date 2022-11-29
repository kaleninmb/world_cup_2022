from django.http import HttpResponse
from django.template import loader
from .controllers import country

# Create your views here.
def index(request):
    template = loader.get_template('wc2022/index.html')
    return HttpResponse(template.render({}, request))

def country_list(request):
    template = loader.get_template('wc2022/country_list.html')
    context = country.country_list()
    return HttpResponse(template.render(context, request))

def country_group(request, country_id):
    template = loader.get_template('wc2022/country_group.html')
    context = country.country_group(country_id)
    return HttpResponse(template.render(context, request))