#!/usr/bin/python

from tornado import ioloop, web, websocket

class WebSocketHandler(websocket.WebSocketHandler):
    def open(self):
        self.write_message('100x100')

    def on_message(self, message):
        print message


application = web.Application([
    ('/ws', WebSocketHandler),
    ('/(.*)', web.StaticFileHandler, {
        'path': 'web',
        'default_filename': 'index.html'
    })
])

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()
