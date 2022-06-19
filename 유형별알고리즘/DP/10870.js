const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = Number(input[0]);
const dp = new Array(20).fill(0);

function fibo(x) {
  if (x === 0) return 0;
  if (x === 1) return 1;
  dp[x] = fibo(x - 1) + fibo(x - 2);
  return dp[x];
}

console.log(fibo(N));
