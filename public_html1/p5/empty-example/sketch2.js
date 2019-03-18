var x, y; //wspolrzedne obiektu
var krok = -1;
function setup() {
  // put setup code here
  createCanvas(600, 600);
  x = 575;
  y = 575;
}

function draw() {
  background(200);

  //r = random(265);
  //g = random(265);
  //b = random(265);
  //stroke(r, g, b);

  fill('#a34cb5');
  strokeWeight(5);
  stroke('black');
  if (x > 14)
     x = x + krok;
     else {
       x = x - krok;
     }
  if (y > 14)
     y = y + krok;
  else{
    y = y - krok;
  }

  ellipse(x, y, 30, 30);







}
