#!/usr/bin/env python3
# coding: utf-8

from view.template import Template


class Page(object):
    def __init__(self):
        self.page = ""
        self.css = "/css/bootstrap.min.css"
        self.hanokh_css = "css/style.css"
        self.js = "/js/bootstrap.bundle.min.js"
        self.page_title = "VPNMGR"
        self.processed_data = ""
    
    def get_page_template(self, file_template):
        template = Template()
        page = ""

        try:
            page = template.read_file(file_template)

        except:
            page = self.page_404()
            
            return page
        
        
        return page
    
    def page_login(self):
        self.page = self.get_page_template('login')
        self.page_title = "Login"

        self.page = str(self.page).format(
            self.page_title,
            self.css,
            self.hanokh_css
        )

        return self.page

    def page_start(self):
        self.page = self.get_page_template('start')
        self.page_title = "Página inicial"
        self.page = str(self.page).format(
            self.page_title,
            self.css,
            self.hanokh_css
        )

        return self.page
    
    def create_user(self):
        self.page = self.get_page_template('create_user')
        self.page_title = "Criar Usuário"
        
        self.page = str(self.page).format(
            self.page_title,
            self.css,
            self.hanokh_css,
            self.js,
            self.processed_data
            )
        
        return self.page
    
    def video_teste(self):
        file = open(proj.BASEPATH + "/view/asssets/teste2.m3u8", "r")
        page = ""
        for line in file.readlines():
            page += line
        
        return page

    def page_404(self):
        self.page = self.get_page_template('404')
        self.page = self.page.format(self.css, self.hanokh_css)

        return self.page
