# coding: utf-8

from django.conf.urls import url, urlpatterns
from jsroutes.views import routes


urlpatterns = [
    url(r"^routes\.js$", routes, name="jsroutes"),
]
