let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

input = input.map((value) => value.split(" ").map((el) => +el));
const [N] = input[0];

const obj = {};
let cnt = 0;

for (let i = 1; i < N + 1; i++) {
  if (input[i][0] in obj && obj[input[i][0]] !== input[i][1]) {
    cnt++;
  }
  obj[input[i][0]] = input[i][1];
}

console.log(cnt);
