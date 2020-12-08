from django.shortcuts import render
from django.shortcuts import reverse

# Create your views here.


def index(request):
    """ Main view to show index page """
    context = {
        'main_title': 'Customer API',
        'usage_url': reverse('customer:api_v1:doc'),
        'github_url': 'https://github.com/jrnp97/customer',
    }
    return render(request, template_name='customer/index.html', context=context)
