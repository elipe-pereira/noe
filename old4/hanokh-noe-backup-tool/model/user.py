#!/usr/bin/python3
# coding: utf-8


class User(object):
    def __init__(self):
        self.user = ""
        self.password = ""

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password
