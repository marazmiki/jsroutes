# coding: utf-8

from django.conf.urls import url, patterns
from jsroutes.views import routes


urlpatterns = patterns('',
    url(r"^routes\.js$", routes, name="jsroutes"),
)

