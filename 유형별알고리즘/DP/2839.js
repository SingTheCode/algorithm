const fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = Number(input[0]);
let minCnt = 10000;

function solution(N) {
  dfs(N, 0);
  if (minCnt === 10000) return -1;
  return minCnt;
}

function dfs(num, cnt) {
  if (num === 0) {
    if (minCnt > cnt) minCnt = cnt;
    return;
  }

  if (minCnt < cnt) return;

  if (num >= 5) dfs(num - 5, cnt + 1);
  if (num >= 3) dfs(num - 3, cnt + 1);
  return;
}

console.log(solution(N));
