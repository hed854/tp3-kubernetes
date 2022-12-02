import psycopg2
import os
import http.server
import socketserver
import logging
import sys


class IndexHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

print("start app")

app_port = os.environ.get("APP_PORT")

connection = psycopg2.connect(
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD"),
        host=os.environ.get("DB_HOST"),
        port=os.environ.get("DB_PORT"),
        database=os.environ.get("DB_NAME")
)

cursor = connection.cursor()

with open("index.html", "w") as f:
    try:
        cursor.execute("SELECT * from test;")
        for i in cursor:
            f.write(f"{i}\n")
    except (Exception, Error) as error:
        print(error)

Handler = IndexHandler

with socketserver.TCPServer(("", int(app_port)), Handler) as httpd:
    print("Serving at port: ", int(app_port))
    httpd.serve_forever()

