function setup() {
  // put setup code here
  createCanvas(700, 600);
}

function draw() {
  // put drawing code here
  fill('#FFCC00');
  strokeWeight(10);
  stroke('#333333');
  ellipse(100, 200, 30, 80);
  fill('#333333');
  strokeWeight(15);
  stroke('#FFCC00');
  ellipse(40, 100, 80, 30);

  strokeWeight(5);
  stroke('black');
  fill('black');
  line(10, 10, 60, 60);
  line(60, 10, 10, 60);

  stroke('blue');
  fill('blue');
  point(100, 100);

  rect(100, 100, 200, 50, 10);



}
