""" Module to define project-level views """
from django.shortcuts import redirect


def redirect_view(request):
    """ Function request to redirect from / route to /fpso/ route """
    return redirect('customer:index')
