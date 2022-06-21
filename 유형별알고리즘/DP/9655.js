const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = Number(input[0]);

function solution(N) {
  if (N % 2 === 0) return "CY";
  else return "SK";
}

console.log(solution(N));
