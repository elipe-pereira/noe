#!/usr/bin/env python3
# coding: utf-8
import proj_config as proj
import psycopg2


class Database(object):
    def __init__(self):
        self.database_username = proj.DATABASE_USER
        self.database_password = proj.DATABASE_PASSWORD
        self.database_name = proj.DATABASE_NAME
        self.database_host = proj.DATABASE_HOST
        self.database_port = proj.DATABASE_PORT

    def get_database_username(self):
        return self.database_username

    def get_database_password(self):
        return self.database_password

    def get_database_name(self):
        return self.database_name

    def get_database_host(self):
        return self.database_host

    def get_database_port(self):
        return self.database_port

    def connect_database(self):
        dsn =  "dbname=" + self.database_name
        dsn += " user=" + self.database_username
        dsn += " password=" + self.database_password
        dsn += " host=" + self.database_host
        dsn += " port=" + self.database_port

        conn = psycopg2.connect(dsn)

        return conn

    def select_username(self, username):
        sql = """SELECT username, password
                FROM person
                    WHERE username='{0}';""".format(username)

        conn = self.connect_database()
        cur = conn.cursor()

        try:
            cur.execute(sql)


        except:
            print("Usuario " + username +  " nao encontrado")

        result = cur.fetchone()
        
        cur.close()
        conn.close()

        return result
