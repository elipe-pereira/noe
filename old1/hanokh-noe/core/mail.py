#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


class Mail(object):
	def __init__(self, hora_inicio, hora_fim, section):
		self.hora_inicio = hora_inicio
		self.hora_fim = hora_fim
		self.section = section

		self.message = """
		<!DOCTYPE html>
		<html>
			<head>
				<meta charset='utf-8'>
				<title>
					Mensagem
				</title>
				<style>
					h1{{
						color: blue;
					}}

					table{{
						border: 1px solid black;
					}}

					td{{
						padding: 5px;
						font-size:14px;
					}}

					.titulo-table{{
						font-weight: bold;
						font-size: 18px;

					}}

					.linha-horizontal{{
						border-bottom: 1px solid #ddd;
					}}
				</style>
			</head>
			<body>
				<h1>Hanokh Software Labs</h1>
				<hr>
				<table>
					<tr>
						<td class="titulo-table linha-horizontal">
							Horário de início
						</td>
						<td class="titulo-table linha-horizontal">
							Horário de términdo
						</td>
						<td class="titulo-table linha-horizontal">
							Rotina
						</td>
					</tr>
					<tr>
						<td>
							'{0}'
						</td>
						<td>
							'{1}'
						</td>
						<td>
							'{2}'
						</td>
					</tr>
				</table>
			</body>
		</html>
		""".format(self.hora_inicio, self.hora_fim, self.section)

	
	def send(self, subject, mail_address):
		os.system("test -d /`whoami`/Mail || mkdir /`whoami`/Mail ")
		os.system("echo '{0}' | mutt -e 'set content_type=text/html' -F /etc/noe/muttrc -s '{1}' {2}".format(
			self.message, subject, mail_address
			))