#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import proj_config as proj

class Template:
	def __init__(self):
		self.basepath = proj.BASEPATH
		self.template_folder = "/view/templates/" + proj.TEMPLATE_NAME
		self.folder_templates =  self.basepath + self.template_folder + "/"


	def read_file(self, file_template):
		file_template = self.folder_templates + file_template + ".html"
		file = open(file_template, 'r', encoding='utf-8')
		page = ""

		for html in file.readlines():
			page = page + html

		file.close()

		return page
