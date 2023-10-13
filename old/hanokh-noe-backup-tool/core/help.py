#!/usr/bin/env python3
# coding: utf-8

class Help(object):
	def __init__(self):
		self.menu = """
USAGE:
	noe [backup-routine]

	default: print help

PARAMETERS:

	--list-routines	- Lista das rotinas configuradas em noe.conf.
	--backup-all	- Faz backup de todas as rotinas listadas se houverem.
	--help		- Mostra este help.
	routine 	- Executa uma das rotinas configuradas e que podem
			ser listadas com o comando --list-routines. 

		"""

	def get_help(self):
		return self.menu