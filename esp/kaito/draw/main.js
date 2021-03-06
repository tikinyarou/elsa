var canvas = document.getElementById('canvas');
var context = canvas.getContext('2d');

var radius = 5;
var dragging = false;

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

context.lineWidth = radius*2;

var putPoint = function(e){
  if(dragging){
    context.lineTo(e.offsetX, e.offsetY);
    context.stroke();
    context.beginPath();
    context.arc(e.offsetX, e.offsetY, radius, 0, Math.PI*2);
    context.fill();
    context.beginPath();
    context.moveTo(e.offsetX, e.offsetY);
 }
}

var engage = function(e){
  dragging = true;
  putPoint(e);
}

var disengage = function(){
  dragging = false;
  context.beginPath();
}

// 音楽ビジネスに関するwebの記事　国内外問わない　一年以内　
// わからない事をまとめる
canvas.addEventListener('mousedown',engage);
canvas.addEventListener('mousemove',putPoint);
canvas.addEventListener('mouseup',disengage);
