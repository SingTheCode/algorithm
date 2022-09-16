"use strict";

let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M] = input[0].split(" ").map((el) => +el);
const notSumList = input
  .slice(1)
  .map((value) => value.split(" ").map((el) => +el));

function solution(N, M, notSumList) {
  // 겹치지 않게 세가지 고르는 방법 전부 찾아
  const totalCase = [];

  for (let i = 1; i < N - 1; i++) {
    for (let j = i + 1; j < N; j++) {
      for (let k = j + 1; k < N + 1; k++) {
        totalCase.push([i, j, k]);
      }
    }
  }

  const cntCase = new Array(totalCase.length).fill(true);

  // notSumList에 있는 요소 모두 포함하는 경우를 totalCase에서 빼
  notSumList.forEach((compare) => {
    for (let i = 0; i < totalCase.length; i++) {
      let cnt = 0;
      
      // 시간 초과
      for (let j = 0; j < 3; j++) {
        if (compare[0] === totalCase[i][j] || compare[1] === totalCase[i][j]) {
          cnt++;
        }
      }

      if (cnt === 2) {
        cntCase[i] = false;
      }
    }
  });

  const result = cntCase.reduce((prev, cur) => {
    if (cur === true) return prev + 1;
    return prev;
  }, 0);

  return result;
}

console.log(solution(N, M, notSumList));
