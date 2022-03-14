var mainCanvas = document.querySelector("#myCanvas");
var context = mainCanvas.getContext("2d");

var count = 0

function draw(){
    /* this clears the canvas as we draw (x coordinat, y coordinat, width, height ) of the canvas */
    context.clearRect(0, 0, 700, 500);

    count+=5;

    /* (x coordinat, y coordinat, width, height )*/
    context.fillRect(count, 100, 50, 50);
    context.fillStyle = "#003399";/*sets the color of the element selected */

    if(count>800){
        count = -50;
    }

    window.requestAnimationFrame(draw); /*sets the animation to continuioausly animate */
}

draw();/*Call the function */