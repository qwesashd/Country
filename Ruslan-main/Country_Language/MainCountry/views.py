from django.core.paginator import Paginator
from django.shortcuts import render
import json

with open('/home/student/Django1/Country_Language/country-json/src/country-by-languages.json') as json_file:
    json_country = json.load(json_file)

bukvi = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y'


def pagination_add(request, array, len):
    paginator = Paginator(array, len)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def about(request):
    return render(request, 'maincountry/about.html')


def add_country(request):
    array = []
    for i in json_country:
        array.append(i['country'])

    page_obj = pagination_add(request, array, 10)
    array1 = {
        'title': 'Страны',
        'page_object': page_obj,
        'buk': bukvi
    }
    return render(request, 'maincountry/country.html', array1)


def add_language(request):
    array = []
    for i in json_country:
        for j in i['languages']:
            array.append(j)
    array = sorted(set(array))
    page_obj = pagination_add(request, array, 15)
    array1 = {
        'title': 'languages',
        'page_object': page_obj,
        'buk': bukvi
    }
    return render(request, 'maincountry/language.html', array1)


def country_add_languages(request, url):
    array = []
    if url in bukvi:
        for i in json_country:
            if i['country'][0] == url:
                array.append(i['country'])
        page_obj = pagination_add(request, array, 10)
        array1 = {
            'title': url,
            'page_object': page_obj,
            'buk': bukvi
        }
        return render(request, 'maincountry/country.html', array1)
    else:
        for i in json_country:
            if i['country'] == url:
                array = i['languages']
        array1 = {
            'title': 'Languages',
            'array': array,
            'url': url,
            'last': array[-1]
        }
        return render(request, 'maincountry/country_add_languages.html', array1)


def languages_add_country(request, url):
    array = []
    if url in bukvi:
        for i in json_country:
            for j in i['languages']:
                if j[0] == url:
                    array.append(j)
        array = sorted(set(array))
        page_obj = pagination_add(request, array, 15)
        array1 = {
            'title': 'country',
            'page_object': page_obj,
            'buk': bukvi
        }
        return render(request, 'maincountry/language.html', array1)
    else:
        for i in json_country:
            for j in i['languages']:
                if j == url:
                    array.append(i['country'])
        array = sorted(set(array))
        array1 = {
            'title': 'country',
            'array': array,
            'url': url,
            'last': array[-1]
        }
        return render(request, 'maincountry/languages_add_country.html', array1)