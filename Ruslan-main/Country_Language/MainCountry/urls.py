from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('country', views.add_country, name='country'),
    path('language', views.add_language, name='language'),
    path('country/<url>', views.country_add_languages),
    path('language/<url>', views.languages_add_country)
]
