"use strict";

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
  QList.push(Q);
  SList.push(S);
  BList.push(B);
}

function solution(QList, SList, BList) {
  const possibleNumList = new Array(988).fill(true);

  // 123 ~ 987 사이의 모든 수와 Q를 비교해서 strike와 ball 수가 같은 경우가 아니면 false로 변경한다
  function checkNum(Q, S, B) {
    const QStr = String(Q);

    for (let i = 0; i < 988; i++) {
      let strike = 0;
      let ball = 0;
      const compareStr = String(i);

      for (let j = 0; j < 3; j++) {
        for (let k = 0; k < 3; k++) {
          if (QStr[j] === compareStr[k]) {
            if (j === k) {
              strike++;
            } else {
              ball++;
            }
          }
        }
      }

      // 숫자가 최소 2자리 이상 같은 경우 false로 변경한다
      if (
        !(strike === S && ball === B) ||
        compareStr[0] === compareStr[1] ||
        compareStr[1] === compareStr[2] ||
        compareStr[0] === compareStr[2] ||
        compareStr[0] === "0" ||
        compareStr[1] === "0" ||
        compareStr[2] === "0" ||
        compareStr.length < 3
      ) {
        possibleNumList[compareStr] = false;
      }
    }
  }

  for (let p = 0; p < N; p++) {
    checkNum(QList[p], SList[p], BList[p]);
  }

  // possibleNumList에서 true인 숫자의 개수를 반환한다
  const result = possibleNumList.reduce((prev, cur, idx) => {
    if (cur === true) {
      return prev + 1;
    } else return prev;
  }, 0);

  return result;
}

console.log(solution(QList, SList, BList));

// 123부터 찾는 로직을 적고, 123보다 작은 곳에서 해당 로직을 벗어난 곳을 결과값에 넣었다. 범위를 잘 확인해야겠다.
