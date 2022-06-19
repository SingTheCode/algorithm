const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = parseInt(input[0]);
const dp = new Array(100).fill(-1);

function fibo(x) {
  if (x === 0) return 0;
  if (x === 1) return 1;
  if (dp[x] !== -1) return dp[x];
  dp[x] = fibo(x - 1) + fibo(x - 2);
  return dp[x];
}
console.log(fibo(N));

console.log(dp);
