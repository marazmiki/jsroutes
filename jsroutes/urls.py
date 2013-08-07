# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns("jsroutes.views",
    url(r"^routes\.js$", "routes", name="jsroutes"),
)
