#!/usr/bin/env python3
# coding: utf-8

import mimetypes
import proj_config as proj
from model.header import Header
from model.status import Status

class RouteAssets(object):
    def __init__(self):
        self.assets = {
            "/favicon.ico" : proj.BASEPATH + "/view/assets/images/favicon.ico",
            "/css/bootstrap.min.css" : proj.BASEPATH + "/view/assets/css/bootstrap.min.css",
            "/css/style.css" : proj.BASEPATH + "/view/assets/css/style.css",
            "/js/bootstrap.bundle.min.js" : proj.BASEPATH + "/view/assets/js/bootstrap.bundle.min.js",
            "/images/hinata_framework" : proj.BASEPATH + "/view/assets/images/hinata_framework.png"
            }
    
    def is_there_asset(self, route_asset):
        if route_asset in self.assets.keys():
            return True
        
        else:
            return False
    
    
    def get_route_assets(self):
        return self.assets
    
    
    def load_asset(self, route_asset):
        mimetypes.init()
        status = Status()
        header = Header()
        page = ""
        
        if self.is_there_asset(route_asset):
            file = ""
            asset = self.assets[route_asset]
            file_type = mimetypes.guess_type(asset)
            
            print(file_type)
            
            if file_type[0] == "text/css" or file_type[0] == "application/javascript":
                file = open(asset)
                header.set_header([('Content-type', file_type[0])])
                
                for line in file.readlines():
                    page += line
                
                page = bytes(str(page), 'utf-8')
                
                return (page, header.get_header(), status.get_status())
            
            else:
                file = open(asset, 'rb').read()
                
                print(file_type)
                
                if route_asset == "/favicon.ico":
                    header.set_header([('Content-type', "image/x-icon")])
                    
                    return (file, header.get_header(), status.get_status())
                    
                else:
                    header.set_header([('Content-type', file_type[0]), 
                                       ("Content-Length", str(len(file))), 
                                       ("Content-Range", "1000-4000/{0}".format(str(len(file)))), 
                                       ("Transfer-Encoding", "chunked")])
                                        
                    return (file, header.get_header(), status.get_status())       
        
        else:
            return ("""<!DOCTYPE html>
                <html>
                    <head>
                        <title>
                        </title>
                    </head>
                    <body>
                    <h1>Asset nao encontrado</h1>
                    </body>
                </html>
            """, header.get_header(), status.get_status())
            