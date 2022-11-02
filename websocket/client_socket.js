let socket = new WebSocket("ws://127.0.0.1:15001");


// function move() {
//       setTimeout(move(), 1000);
// }
setInterval(function(){ 
  var buffer = new ArrayBuffer(16);
    socket.send([0x4, 0xFF, 0x01, 0x20, 0x0, 0x4, 0xFF, 0x01, 0x20, 0x0]);

}, 1000);