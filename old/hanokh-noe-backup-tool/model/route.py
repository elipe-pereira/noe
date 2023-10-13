#!/usr/bin/env python3
# coding: utf-8

from model.header import Header
from model.status import Status
from model.auth import Auth
from model.page import Page


class Route(object):
    def __init__(self, environ):
        self.environ = environ
        self.route = self.environ['PATH_INFO']
        self.request = self.environ['wsgi.input'].read()
        self.header = Header()
        self.status = Status()
        self.route = environ['PATH_INFO']
        self.response_headers = self.header.get_header()
        self.auth = Auth(self.request, self.header)
        self.page_template = Page()
        self.page = Page()
        self.is_auth = self.auth.is_auth()
          
    def get_route(self):
        if self.is_auth:
            if self.route == "/login":
                html = self.page.page_login()
                page_header = self.header.get_header()
                page_status = self.status.get_status()
                
                return (html, page_header, page_status)
        
            else:
                html = self.page.page_404()
                
                page_header = self.header.get_header()
                page_status = self.status.get_status()
                
                return (html, page_header, page_status)
        
        else:
            if self.route == "/":
                html = self.page.page_start()
                page_header = self.header.get_header()
                page_status = self.status.get_status()

                return (html, page_header, page_status)

            elif self.route == "/login":
                html = self.page.page_login()
                page_header = self.header.get_header()
                page_status = self.status.get_status()
                
                return (html, page_header, page_status)
            
            elif self.route == "/video/teste":
                pass
            
            else:
                html = self.page.page_404()
                
                page_header = self.header.get_header()
                page_status = self.status.get_status()
                
                return (html, page_header, page_status)
