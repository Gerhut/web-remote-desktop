#!/usr/bin/env python

from base64 import b64encode, b64decode
from zlib import decompress
from platform import system

from PIL import Image
import mss
from tornado import ioloop, web, websocket

try:
  from cStringIO import StringIO
except:
  from StringIO import StringIO

__all__ = [
    'Handler'
]

MSS = {
    'Darwin': mss.MSSMac,
    'Linux': mss.MSSLinux,
    'Windows': mss.MSSWindows
}[system()](False)

monitor = None

for m in MSS.enum_display_monitors(-1):
    monitor = m
    break;

size = (monitor['width'], monitor['height'])

def get_data(quality=30):
    data = MSS.get_pixels(monitor)
    
    data = Image.frombytes('RGB', size, data)
    sio = StringIO()
    data.save(sio, 'jpeg', quality=quality)
    data = sio.getvalue()
    sio.close()
    return data

class Handler(websocket.WebSocketHandler):

    clients = set()

    def open(self):
        self.write_message('x'.join(map(str, size)))
        self.__class__.clients.add(self)

    def close(self):
        self.__class__.clients.remove(self)

    @classmethod
    def send(cls, loop):
        try:
            data = get_data(30)
            closed = set()
            for client in cls.clients:
                if client.ws_connection:
                    client.write_message(data, binary=True)
                else:
                    closed.add(client)

            for client in closed:
                client.close()
        finally:
            loop.add_callback(cls.send, loop)

if __name__ == "__main__":
    application = web.Application([('/', Handler)])
    PORT = 7384
    application.listen(PORT)
    print 'Screenshot Service Listening on %d' % (PORT,)
    loop = ioloop.IOLoop.instance()
    loop.add_callback(Handler.send, loop)
    loop.start()
