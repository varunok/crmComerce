# -*- coding: utf-8 -*-


from watson import search as watson
from django.shortcuts import render
from facility.models import ContactOwner
from arendator.models import Arendator
from buyer.models import Buyer
from makler.models import Makler
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def searching(request):
    search_results_facility = watson.filter(ContactOwner, request.GET.get('q'))
    search_results_arendator = watson.filter(Arendator, request.GET.get('q'))
    search_results_buyer = watson.filter(Buyer, request.GET.get('q'))
    search_results_makler = watson.filter(Makler, request.GET.get('q'))
    return render(request, 'searching/search_results.html', {'search_results_facility': search_results_facility,
                                                             'search_results_arendator': search_results_arendator,
                                                             'search_results_buyer': search_results_buyer,
                                                             'search_results_makler': search_results_makler})
