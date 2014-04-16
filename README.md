Web Remote Desktop
==================

毕设第二个版本。。用Tornado实现远程桌面
为了提升性能，截图和鼠标操作均采用原生方式实现

- Windows使用WIN32API
- Linux使用读取dev文件

Dependency
----------

- Python 2.7
- Tornado
- autopy

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
