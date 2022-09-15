'use strict';

let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const QList = [];
const SList = [];
const BList = [];

const N = Number(input[0]);

for (let i = 1; i < N + 1; i++) {
  const [Q, S, B] = input[i].split(" ").map((el) => +el);
  QList.push(String(Q).split(""));
  SList.push(S);
  BList.push(B);
}

function solution(QList, SList, BList) {
  let result = 0;

  function dfs(Q, cnt, num) {
    if (cnt === N) {
      const spaceCnt = num.filter((char) => char === undefined);
    }
  }
}

console.log(solution(QList, SList, BList));
