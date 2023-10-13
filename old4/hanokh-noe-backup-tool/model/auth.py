#!/usr/bin/python3
# coding: utf-8

from urllib.parse import parse_qs
from model.database import Database
import hashlib

class Auth(object):
    def __init__(self, request, header):
        self.request = request
        self.header = header
        self.user_input = ""
        self.pass_input = ""
        self.hash_access_input = ""
        self.valid_user_hash = ""
        self.database = Database()
        self.user_search = ""
        self.cookie = ""
        self.ssid = ""
        self.user_cookie = ""
    
    
    def is_auth(self):
        request = parse_qs(self.request)
        print("-" * 25)
        print(request)
        
        try:
            self.user_input = request[b'username'][0]
            print(self.user_input)
        
        except:
            print("Usuario não informado nessa solicitação")
        
        try:
            self.pass_input = request[b'password'][0]
            print(self.pass_input)
        
        except:
            print("Senha não informada nesta solicitação")
        
        join_user_pass = self.user_input + self.pass_input
        print(join_user_pass)
        
        if len(join_user_pass) > 0:
            self.hash_access_input = hashlib.sha512(join_user_pass).hexdigest()
            print("Gerando o hash do input do usuário")
            
        
        if len(self.user_input) > 0:
            self.user_input = self.user_input.decode()
            print("Faz o decode para string do nome do usuario")
        
        self.user_search = self.database.select_username(self.user_input)
        print(self.user_search)
        
        if self.user_search:
            self.valid_user_hash = self.user_search[1]
        
        if len(self.valid_user_hash) > 0 and len(self.hash_access_input) > 0:
            if self.valid_user_hash == self.hash_access_input:
                self.header.set_header([('Content-type', 'text/html'), 
                                        ('set-cookie', 'SSID=' + self.hash_access_input),
                                        ('set-cookie', 'USER=' + self.user_input)])
                
                print("True")
                return True
            
            else:
                self.header.set_header([('Content-type', 'text/html'), 
                                        ('set-cookie', 'SSID='),
                                        ('set-cookie', 'USER=')])
                
                return False
        
        else:
            try:
                self.cookie = self.environ['HTTP_COOKIE'].split(" ")
                print(self.cookie)
                self.ssid = parse_qs(self.cookie[0])
                self.ssid = self.ssid['SSID'][0]
                print(self.ssid)
                self.user_cookie = parse_qs(self.cookie[1])
                self.user_cookie = self.user_cookie['USER'][0]
                print(self.user_cookie)
            
            except:
                print("Não há cookie salvo")
                print("Ou outro erro desconhecido")
                return False
            
            try:
                self.user_search = self.database.select_username(self.user_cookie)
            
            except:
                print("Não foram encontrados dados do cookie pesquisado")
                return False
            
            
            try:
                self.valid_user_hash = str(self.user_search[1])
                print(self.valid_user_hash)
            
            except:
                print("Hash password não encontrado")
                
            if self.valid_user_hash == "":
                return False
            
            if self.valid_user_hash == self.ssid:
                return True
            
            else:
                print("AQui")
                self.header.set_header([('Content-type', 'text/html'), 
                                        ('set-cookie', 'SSID='), 
                                        ('set-cookie', 'USER=')])
                
                return False
