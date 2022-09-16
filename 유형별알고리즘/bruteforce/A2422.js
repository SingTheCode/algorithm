"use strict";

let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M] = input[0].split(" ").map((el) => +el);
const badChoice = new Array(N).fill(false);
input
  .slice(1)
  .map((value) => value.split(" ").map(Number))
  .forEach((w) => {
    const [x, y] = w;
    badChoice[x - 1][y - 1] = true;
    badChoice[y - 1][x - 1] = false;
  });

function solution(N, M, notSumList) {
  let result = 0;

  for (let i = 1; i < N - 2; i++) {
    for (let j = i + 1; j < N - 1; j++) {
      if (badChoice[i][j]) continue;
      for (let k = j + 1; k < N; k++) {
        if (badChoice[j][k] || badChoice[i][k]) continue;
        result++;
      }
    }
  }

  return result;
}

console.log(solution(N, M, notSumList));
