# -*- coding: utf-8 -*-


import psycopg2
from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
from django.conf import settings
from facility.models import AddressFacilityData
from arendator.models import Arendator
from buyer.models import Buyer
from makler.models import Makler
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def searching(request):
    search_results_f = SearchPostgres().search_fts(request.GET.get('search_text'), 'facility_addressfacilitydata')
    search_results_co = SearchPostgres().search_fts(request.GET.get('search_text'), 'facility_contactowner')
    facility = get_address_facility(search_results_co, search_results_f)
    search_results_a = SearchPostgres().search_fts(request.GET.get('search_text'), 'arendator_arendator')
    search_results_b = SearchPostgres().search_fts(request.GET.get('search_text'), 'buyer_buyer')
    search_results_m = SearchPostgres().search_fts(request.GET.get('search_text'), 'makler_makler')
    try:
        phone = int(request.GET.get('search_text'))
        search_phone_a = Arendator.objects.filter(phone_first__istartswith=phone)
        search_phone_b = Buyer.objects.filter(phone_first__istartswith=phone)
        search_phone_m = Makler.objects.filter(phone_first__istartswith=phone)
    except:
        search_phone_a = ''
        search_phone_b = ''
        search_phone_m = ''
    return render(request, 'searching/search_results.html', {'search_results_facility': facility,
                                                             'search_results_arendator': search_results_a,
                                                             'search_phone_arendator': search_phone_a,
                                                             'search_results_buyer': search_results_b,
                                                             'search_phone_buyer': search_phone_b,
                                                             'search_results_makler': search_results_m,
                                                             'search_phone_makler': search_phone_m})


def get_addres_id(search_results_f):
    list_id = []
    for result in search_results_f:
        id_f = result.get('id')
        list_id.append(id_f)
    return list_id


def get_address_facility(search_results, search_results_f):
    f_list_id = get_addres_id(search_results_f)
    for result in search_results:
        id_co = result.get('addressfacilitydata_ptr_id')
        if id_co not in f_list_id:
            f_list_id.append(id_co)
    facility = AddressFacilityData.objects.filter(id__in=f_list_id)
    return facility


class SearchPostgres(object):
    """docstring for SearchPostgres"""

    def __init__(self):
        super(SearchPostgres, self).__init__()
        # self.arg = arg
        conn_string = "host='localhost' dbname='{0}' user='{1}' password='{2}'".format(
            settings.DATABASES['default']['NAME'],
            settings.DATABASES['default']['USER'],
            settings.DATABASES['default']['PASSWORD'])
        self.connection = psycopg2.connect(conn_string)

    def search_fts(self, search_text, table):
        self.search_text = search_text
        # self.query = "SELECT phone_owner, name_owner, phone_owner_plus," \
        #              " ts_headline('russian', name_owner, query, 'StartSel = <b>, StopSel = </b>, " \
        #              "MaxFragments=2, ShortWord=0,FragmentDelimiter=<p></p>') AS headline, rank FROM "
        # self.sub_query = "(SELECT phone_owner, name_owner, phone_owner_plus, query," \
        #                  " ts_rank_cd(fts, query) AS rank FROM facility_contactowner, to_tsquery(%s) query" \
        #                  " WHERE fts @@ query ORDER BY rank DESC LIMIT 10)  AS fts_search;"
        self.query = "SELECT * FROM " + table + " WHERE fts @@ to_tsquery(%s);"
        results = self._serch_fts_ao('&')
        if not results:
            results = self._serch_fts_ao('|')
        return results

    def _serch_fts_ao(self, operator):
        results = []
        operator = ":*" + operator
        with self.connection.cursor() as cursor:
            # cursor.execute(self.query + self.sub_query, [operator.join(self.search_text.split())])
            if len(self.search_text.split()) > 1:
                cursor.execute(self.query, [operator.join(self.search_text.split())])
            else:
                cursor.execute(self.query, [''.join([self.search_text.strip(), ':*'])])
            desc = cursor.description
            rows = cursor.fetchall()

            for row in rows:
                results.append(dict(zip([col[0] for col in desc], row)))
        # print(results)
        return results
