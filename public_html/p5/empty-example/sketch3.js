var x, y; // współrzędne obiektu
var krok = -1;
function setup() {
  // put setup code here
  createCanvas(600, 600);
  background(200);

}

function draw() {

  noFill();
  noStroke();

  if (mouseIsPressed) { //nacisnieto klawisz myszki
    if (mouseButton === LEFT) {
    fill('#a34cb5');
    strokeWeight(5);
    stroke('black');
    }
    if (mouseButton === CENTER) {
      strokeweight(15);
      fill(200);
      stroke(200);
      rect(mouseX- 10, mouseY- 10, 20, 20);
    }
  }
  point(mouseX, mouseY);
  //r = random(265);
  //g = random(265);
  //b = random(265);
  //stroke(r, g, b);












}
