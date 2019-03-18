var length = 30;
x = y = 100;
function setup() {
  x = y = 30
  // put setup code here
  createCanvas(600, 600);


}

function draw() {
  background(200);
  dx = mouseX - x;
  dy = mouseY - y;
angle1 = atan2(dy, dx);
x = mouseX - (cos(angle1) * lenght);
y = mouseY - (sin(angle1) * lenght);
rect(x, y, 30, 30);
  }

  //r = random(265);
  //g = random(265);
  //b = random(265);
  //stroke(r, g, b);












}
