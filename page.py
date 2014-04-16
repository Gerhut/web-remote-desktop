#!/usr/bin/env python

from tornado import ioloop, web

import screenshot, control

if __name__ == "__main__":
    application = web.Application([('/(.*)', web.StaticFileHandler, {
        'path': 'web',
        'default_filename': 'index.html'
    })])
    PORT = 8080
    application.listen(PORT)
    print 'Page Service Listening on %d' % (PORT,)
    ioloop.IOLoop.current().start()
