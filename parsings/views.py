# -*- coding: utf-8 -*-


import json
import re
import datetime
# from textblob import TextBlob
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from setting_globall.models import FranshiseSity
from parser_olx import ParserOLX, mutable_month, mutable_phone, valid_categories_list
from makler.models import Makler
from facility.models import ContactOwner
from parsings.models import ConfigParserOLX
from django.contrib.auth.decorators import login_required
from django.conf import settings

# Create your views here.

try:
    config_parser = ConfigParserOLX.objects.get(id=1)
except:
    class config_parser():
        SITE_URL = 'http://google.com'
        AJAX_PHONE = '/ajax'
        SELECTOR_GETLINK_ARTICLES = '//a/@href'
        SELECTOR_GETLINK_CATEGORIES = '//a/@href'
        SELECTOR_GETTEXT_CATEGORIES = '//text()'
        SELECTOR_SITY = '//text()'
        SELECTOR_TITLE = '//text()'
        SELECTOR_DATE = '//text()'


SITE_URL = config_parser.SITE_URL
AJAX_PHONE = config_parser.AJAX_PHONE
SELECTOR_GETLINK_CATEGORIES = config_parser.SELECTOR_GETLINK_CATEGORIES
SELECTOR_GETTEXT_CATEGORIES = config_parser.SELECTOR_GETTEXT_CATEGORIES
# SELECTOR_GETTEXT_CATEGORIES = '//div[@id="bottom1"]//ul//li//a//span[@class="block link category-name"]//span/text()'
SELECTOR_GETLINK_ARTICLES = config_parser.SELECTOR_GETLINK_ARTICLES
# SELECTOR_GETLINK_ARTICLES = '//a[@class="marginright5 link linkWithHash detailsLink"]/@href'
SELECTOR_SITY = config_parser.SELECTOR_SITY
# SELECTOR_SITY = '//a[@class="show-map-link"]//strong/text()'
SELECTOR_TITLE = config_parser.SELECTOR_TITLE
# SELECTOR_TITLE = '//div[@class="offer-titlebox"]//h1/text()'
SELECTOR_DATE = config_parser.SELECTOR_DATE
# SELECTOR_DATE = '//div[@class="offer-titlebox__details"]//em/text()'


@login_required
def services(request):
    if settings.ALLOWED_HOSTS[0] == 'dom6.usatba-krm.dn.ua':
        hi_dn_ua = True
    else:
        hi_dn_ua = False
    return render(request, 'parsings/services.html', {'hi_dn_ua': hi_dn_ua})


@login_required
def parser_olx(request):
    list_categories_text = ParserOLX(SITE_URL).gettext(SELECTOR_GETTEXT_CATEGORIES)
    for cat in list_categories_text:
        dict_categories_text = dict(zip([list_categories_text.index(j) for j in list_categories_text], list_categories_text))
    try:
        sity = ConfigParserOLX.objects.get(id=1)
    except:
        sity = ''
    dict_categories_text = valid_categories_list(dict_categories_text)
    return render(request, 'parsings/parser_olx.html', {"list_categories_text": dict_categories_text,
                                                        "sity": sity})



@login_required
def parse(request):
    try:
        if request.method == 'POST':
            if request.POST['id_sity']:
                sity = ConfigParserOLX.objects.get(id=1)
                sity = sity.SITY
                day_art = timezone.now() - datetime.timedelta(days=int(request.POST['id_term']))
                parse_categories = ParserOLX(SITE_URL).getlink(SELECTOR_GETLINK_CATEGORIES)[
                    int(request.POST['id_categories'])]
                if request.POST['id_sity']:
                        # sity = ConfigParserOLX.objects.get(id=1)
                        # sity = TextBlob(unicode(sity.SITY)).translate()
                        # sity = 'kiev'
                    parse_categories = ''.join([parse_categories, sity.lower(), '/'])
                dict_article = {}
                for page in xrange(int(request.POST['id_page']), int(request.POST['id_page']) + 1):
                    list_article = ParserOLX(''.join([parse_categories, '?page=', str(page)])).getlink(SELECTOR_GETLINK_ARTICLES)
                    count_braek = 0
                    for article in list_article:
                        id_article = article.split('.')[-2].split('-')[-1]
                        page_article = ParserOLX(article)
                        date_article = ' '.join(page_article.gettext(SELECTOR_DATE)).encode('utf-8')
                        p = re.compile(ur'(?P<time_art>\d{2}[:]\d{2})')
                        time_art = re.search(p, date_article)
                        time_art = time_art.group().split(':')
                        p = re.compile(ur'(?P<date_art>\d{1,2}\s\W+\d{4})')
                        date_art = re.search(p, date_article)
                        date_art = date_art.group().split(' ')
                        date_art.reverse()
                        date_art[1] = mutable_month(date_art[1])
                        datetime_art = datetime.datetime(int(date_art[0]), int(date_art[1]), int(date_art[2]),
                                                         hour=int(time_art[0]), minute=int(time_art[1]))
                        if datetime_art > day_art:
                            phone = ParserOLX(SITE_URL + AJAX_PHONE + id_article[2:]).gettext()
                            phone = ''.join(phone)
                            try:
                                phone = json.loads(phone)
                                phone = mutable_phone(phone['value'])
                            except:
                                phone = ['000000']
                            if request.POST['id_except'] == '1' and not Makler.objects.filter(phone__in=phone):
                                dict_article[id_article] = {
                                    'sity': page_article.gettext(SELECTOR_SITY)[0].split(',')[0].split(' ')[-1],
                                    'title': page_article.gettext(SELECTOR_TITLE)[0].strip(),
                                    'link': article,
                                    'phone': phone}
                            elif request.POST['id_except'] == '2' and not ContactOwner.objects.filter(
                                    phone_owner=[int(i) for i in phone]) and not ContactOwner.objects.filter(
                                    phone_owner_plus=[int(i) for i in phone]):
                                dict_article[id_article] = {
                                    'sity': page_article.gettext(SELECTOR_SITY)[0].split(',')[0].split(' ')[-1],
                                    'title': page_article.gettext(SELECTOR_TITLE)[0].strip(), 'link': article, 'phone': phone}
                            elif request.POST['id_except'] == '3' and not Makler.objects.filter(
                                    phone__in=phone) and not ContactOwner.objects.filter(
                                    phone_owner=[int(i) for i in phone]) and not ContactOwner.objects.filter(
                                    phone_owner_plus=[int(i) for i in phone]):
                                dict_article[id_article] = {
                                    'sity': page_article.gettext(SELECTOR_SITY)[0].split(',')[0].split(' ')[-1],
                                    'title': page_article.gettext(SELECTOR_TITLE)[0].strip(), 'link': article, 'phone': phone}
                        else:
                            count_braek += 1
                    if count_braek > 10:
                        break
                dict_article['id_page'] = page + 1
                return HttpResponse(JsonResponse(dict_article))
        else:
            return HttpResponse(status=503)
    except:
        return HttpResponse(status=503)


@login_required
def setting_olx(request):
    try:
        config_parser = ConfigParserOLX.objects.get(id=1)
    except:
        config_parser = ''
    return render(request, 'parsings/setting_olx.html',
                  {'config_parser': config_parser})


@login_required
def sity_conf(request):
    if request.method == 'POST':
        SITY = ConfigParserOLX.objects.get(id=1)
        SITY.SITY = request.POST['sity_conf']
        SITY.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def site_url(request):
    if request.method == 'POST':
        SITE_URL = ConfigParserOLX(id=1, SITE_URL=request.POST['SITE_URL'])
        # SITE_URL = ConfigParserOLX.objects.get(id=1)
        # SITE_URL.SITE_URL = request.POST['SITE_URL']
        SITE_URL.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def ajax_phone(request):
    if request.method == 'POST':
        AJAX_PHONE = ConfigParserOLX.objects.get(id=1)
        AJAX_PHONE.AJAX_PHONE = request.POST['AJAX_PHONE']
        AJAX_PHONE.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_getlink_categories(request):
    if request.method == 'POST':
        SELECTOR_GETLINK_CATEGORIES = ConfigParserOLX.objects.get(id=1)
        SELECTOR_GETLINK_CATEGORIES.SELECTOR_GETLINK_CATEGORIES = request.POST['SELECTOR_GETLINK_CATEGORIES']
        SELECTOR_GETLINK_CATEGORIES.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_gettext_categories(request):
    if request.method == 'POST':
        SELECTOR_GETTEXT_CATEGORIES = ConfigParserOLX.objects.get(id=1)
        SELECTOR_GETTEXT_CATEGORIES.SELECTOR_GETTEXT_CATEGORIES = request.POST['SELECTOR_GETTEXT_CATEGORIES']
        SELECTOR_GETTEXT_CATEGORIES.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_getlink_articles(request):
    if request.method == 'POST':
        SELECTOR_GETLINK_ARTICLES = ConfigParserOLX.objects.get(id=1)
        SELECTOR_GETLINK_ARTICLES.SELECTOR_GETLINK_ARTICLES = request.POST['SELECTOR_GETLINK_ARTICLES']
        SELECTOR_GETLINK_ARTICLES.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_sity(request):
    if request.method == 'POST':
        SELECTOR_SITY = ConfigParserOLX.objects.get(id=1)
        SELECTOR_SITY.SELECTOR_SITY = request.POST['SELECTOR_SITY']
        SELECTOR_SITY.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_title(request):
    if request.method == 'POST':
        SELECTOR_TITLE = ConfigParserOLX.objects.get(id=1)
        SELECTOR_TITLE.SELECTOR_TITLE = request.POST['SELECTOR_TITLE']
        SELECTOR_TITLE.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)


@login_required
def selector_date(request):
    if request.method == 'POST':
        SELECTOR_DATE = ConfigParserOLX.objects.get(id=1)
        SELECTOR_DATE.SELECTOR_DATE = request.POST['SELECTOR_DATE']
        SELECTOR_DATE.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=503)

@login_required
def parser_hi_dn_ua(request):
    return render(request, 'parsings/parser_hi_dn_ua.html', {})


@login_required
def parsehidnua(request):
    if request.method == 'POST':
        id_part = int(request.POST.get('id_part'))
        if id_part == 1:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=56'
        elif id_part == 2:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=9'
        elif id_part == 3:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=11'
        elif id_part == 4:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=12'
        elif id_part == 5:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=13'
        elif id_part == 6:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=19'
        elif id_part == 7:
            link = 'http://hi.dn.ua/index.php?option=com_sobi2&catid=55'
        pages = ParserOLX(link).getlink('//ul[@class="pagination"]/li/strong/a//@href')
        site = ParserOLX(link).gettext(selector='//td//text()')
        if int(request.POST['id_page']) > 1:
            site = ParserOLX(pages[int(request.POST['id_page'])-2]).gettext(selector='//td//text()')
        dict_article = {}
        for articles in site:
            if u'Тел.:' in articles or u'Тел. :' in articles:
                article = articles.split(u'Тел.:')[0]
                phone = articles.split(u'Тел.:')[-1][1:]
                try:
                    phone = ''.join(mutable_phone(phone))
                except:
                    phone = '000000'
                if request.POST['id_except'] == '1' and not Makler.objects.filter(phone__istartswith=phone):
                    dict_article[site.index(articles)] = {'phone': phone.encode('utf8'), 'article': article.encode('utf8')}
                elif request.POST['id_except'] == '2' and not ContactOwner.objects.filter(
                                    phone_owner=[int(i) for i in phone]) and not ContactOwner.objects.filter(
                                    phone_owner_plus=[int(i) for i in phone]):
                    dict_article[site.index(articles)] = {'phone': phone.encode('utf8'), 'article': article.encode('utf8')}
                elif request.POST['id_except'] == '3' and not Makler.objects.filter(
                                    phone__istartswith=phone) and not ContactOwner.objects.filter(
                                    phone_owner=[int(i) for i in phone]) and not ContactOwner.objects.filter(
                                    phone_owner_plus=[int(i) for i in phone]):
                    dict_article[site.index(articles)] = {'phone': phone.encode('utf8'), 'article': article.encode('utf8')}
    dict_article['id_page'] = int(request.POST['id_page']) + 1
    return HttpResponse(JsonResponse(dict_article))
    # return HttpResponse(content=b'ok')
