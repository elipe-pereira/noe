#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.route import Route
from view.route_assets import RouteAssets
import proj_config as proj
proj.insert_basepath_on_python_path()


def application(environ, start_response):
    page = ""
    route = ""
    data = ""
    route_assets = RouteAssets()
    is_asset = route_assets.is_there_asset(environ['PATH_INFO'])

    if is_asset:
        data = route_assets.load_asset(environ['PATH_INFO'])
        page = data[0]
    else:
        route = Route(environ)
        data = route.get_route()
        page = bytes(str(data[0]), "utf-8")

    response_headers = data[1]

    status = data[2]

    start_response(status, response_headers)

    return iter([page])
