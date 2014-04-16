void function () {
  var canvas = document.getElementsByTagName('canvas')[0]
  var context = canvas.getContext('2d')

  var screenshotServer = new WebSocket('ws://' + location.hostname + ':7384/')
  screenshotServer.binaryType = 'arraybuffer'

  screenshotServer.onopen = function() {
    screenshotServer.onmessage = function (event) {
      var size = event.data.split('x')
      canvas.width = size[0]
      canvas.height = size[1]

      function onmessage (event) {
        var image = new Image()
        image.onload = function () {
          context.drawImage(image, 0, 0)
        }
        image.src = 'data:image/jpeg;base64,' + 
          btoa(String.fromCharCode.apply(null, new Uint8Array(event.data)))
      }
      screenshotServer.onmessage = onmessage
    }
  }

  screenshotServer.onclose = function() {
    confirm('Disconnected. Refresh?') && location.reload(true)
  }

  var controlSocket = new WebSocket('ws://' + location.hostname + ':7483/')
  
  controlSocket.onopen = function() {
    function mouse(event) {
      var x = event.pageX || event.changedTouches[0].pageX
      var y = event.pageY || event.changedTouches[0].pageY
      x = Math.round(x / canvas.offsetWidth * canvas.width)
      y = Math.round(y / canvas.offsetHeight * canvas.height)
      switch (event.type) {
        case 'touchstart':
        case 'mousedown':
          cmd = 'd'
          break;
        case 'touchmove':
        case 'mousemove':
          cmd = 'm'
          break;
        case 'touchend':
        case 'touchcancel':
        case 'mouseup':
          cmd = 'u'
          break;
      }
      controlSocket.send(cmd + x + ',' + y)
    }

    if ('ontouchstart' in document) {
      document.ontouchstart = function(event) {
        event.preventDefault();
      }

      canvas.ontouchstart = 
      canvas.ontouchmove =
      canvas.ontouchend = mouse
    } else {
      canvas.onmousedown =
      canvas.onmousemove =
      canvas.onmouseup = mouse
    }
  }

  controlSocket.onclose = function() {
    confirm('Disconnected. Refresh?') && location.reload(true)
  }
} ()