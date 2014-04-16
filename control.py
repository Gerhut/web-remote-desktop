#!/usr/bin/env python

from autopy import mouse
from tornado import ioloop, web, websocket

__all__ = [
    'Handler'
]

def mouse_down(x, y):
    mouse.move(x, y)
    mouse.toggle(True)

def mouse_move(x, y):
    mouse.move(x, y)

def mouse_up(x, y):
    mouse.move(x, y)
    mouse.toggle(False)

class Handler(websocket.WebSocketHandler):

    cmd_to_func = { 'm': mouse_move,
                    'd': mouse_down,
                    'u': mouse_up }

    def on_message(self, message):
        cmd = message[0]
        pos = map(int, message[1:].split(','))
        self.__class__.cmd_to_func[cmd](*pos)

if __name__ == "__main__":
    application = web.Application([('/', Handler)])
    PORT = 7483
    application.listen(PORT)
    print 'Control Service Listening on %d' % (PORT,)
    ioloop.IOLoop.instance().start()
