const fs = require("fs");
const input = fs.readFileSync("stdin").toString().split("\n");
const maze = [];

const [x, y] = input[0].split(" ");
console.log(x, y);

for (let i = 1; i <= x; i++) {
  let temp = input[i].split("");
  maze.push(temp);
}
