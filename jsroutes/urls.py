# coding: utf-8

from django.conf.urls import url
from jsroutes.views import routes


urlpatterns = [
    url(r"^routes\.js$", routes, name="jsroutes"),
]
