#!/usr/bin/env python3
# coding: utf-8

from wsgiref.simple_server import make_server


class Main:
    def __init__(self):
        self.status = "200 OK"
        self.headers = [("Content-type", "text/html; charset=utf-8")]

    def noe(self, environ, start_response):
        start_response(self.status, self.headers)
        texto = str(environ.items()).encode("utf-8")
        # return  [b"Ola mundo"]
        return [texto]

    def run(self):
        with make_server("", 8000, self.noe) as httpd:
            print("Rodando servidor na porta 8000")
            print("Pressione control-C para parar")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("Desligando...")
                httpd.server_close()


if __name__ == "__main__":
    app = Main()
    app.run()
