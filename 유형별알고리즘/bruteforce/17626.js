"use strict";

let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const N = Number(input[0]);

function solution(N) {
  let minCnt = 50000;

  function dfs(cnt, sum) {
    console.log(cnt, sum);
    const dp = new Array(100000).fill(0);

    if (sum > N) return dp[sum];

    if (sum === N) {
      if (minCnt > cnt) minCnt = cnt;
      return dp[sum];
    }

    if (dp[sum] !== 0) return dp[sum];

    for (let i = 1; i < parseInt(N / 2); i++) {
      dp[sum] = dfs(cnt + 1, sum + i ** 2);
    }
  }
  dfs(0, 0);

  return minCnt;
}

solution(N);
