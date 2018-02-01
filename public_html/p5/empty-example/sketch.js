function setup() {
  // put setup code here
  createCanvas(700, 600);
}

function draw() {
  // put drawing code her
  fill('#a34cb5');
  strokeWeight(10);
  stroke('black');
  ellipse(100, 200, 30, 80);
  fill('#75b2d8');
  stroke('pink');
  ellipse(80, 100, 80, 30);

  strokeWeight(5);
  stroke('black');
  fill('black');
  line(10, 10, 60, 60);
  line(60, 10, 10, 60);

  stroke('blue');
  fill('blue');
  point(100, 100);

  rect(200, 200, 300, 100, 10);




}
