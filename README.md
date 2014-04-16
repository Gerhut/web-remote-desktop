Web Remote Desktop
==================

毕设第二个版本。。用Tornado实现远程桌面

Dependency
----------

- Python 2.7
- Tornado
- autopy
- Pillow

Protocol
--------

### Screenshot

Server to client
- String: Screen size, format `<width>x<height>`
- Binary: Screenshot, jpeg format

### Mouse Control

Client to Server
- `d<x>,<y>`: Mouse down
- `m<x>,<y>`: Mouse move
- `u<x>,<y>`: Mouse up
