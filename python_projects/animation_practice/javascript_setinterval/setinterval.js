var car = document.getElementById('car');

var cur = 0;
var dest = 700;
var friction = 0.05;

function loop(){
    cur += (dest-cur) * friction;
    car.style.left = cur + 'px';
    car.style.width = (cur*.5) + 'px';
    //you can set this to differnt styles//
    console.log(cur);
    if(cur >= dest-.1){
        friction = -.05;
        //clearIntervalvar(myLoop);
    }
    if(cur < 1){
        friction = 0.05;
    }
}

var myLoop = setInterval(loop, 20);``