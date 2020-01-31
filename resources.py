#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from coapthon.resources.resource import Resource

# Implement child resources (Pressure, Temperature and Humidity). Reference:


class Temperature(Resource):

    def __init__(self, name="TemperatureResource", coap_server=None):
        super(Temperature, self).__init__(name, coap_server, visible=True,
                                          observable=True, allow_children=True)
        self.payload = "{Temperature Reading: 75℃}"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = Temperature()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True


class Humidity(Resource):
    def __init__(self, name="HumiditySensor", coap_server=None):
        super(Humidity, self).__init__(name, coap_server, visible=True,
                                       observable=True, allow_children=True)
        self.payload = "{Humidity Reading: 80%}"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = Humidity()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True


class Pressure(Resource):
    def __init__(self, name="HumiditySensor", coap_server=None):
        super(Pressure, self).__init__(name, coap_server, visible=True,
                                       observable=True, allow_children=True)
        self.payload = "{Humidity Reading: 80%}"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

    def render_POST(self, request):
        res = Humidity()
        res.location_query = request.uri_query
        res.payload = request.payload
        return res

    def render_DELETE(self, request):
        return True
