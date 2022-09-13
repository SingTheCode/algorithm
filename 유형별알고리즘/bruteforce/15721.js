let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const A = Number(input[0]);
const T = Number(input[1]);
const isDegi = Number(input[2]);

function solution(A, T, isDegi) {
  let repeat = 2;
  let repeatCnt = 0;
  let bunCnt = 0;
  let degiCnt = 0;
  let guho = 0;
  let i = 0;

  while (true) {
    if (i === A) i = 0;
    if (repeatCnt === 4 + repeat * 2) {
      repeatCnt = 0;
      repeat++;
    }

    // 번데기 구호 결정
    if (repeatCnt < 4) {
      guho = repeatCnt % 2;
    } else {
      if (repeatCnt - 4 < repeat) guho = 0;
      else guho = 1;
    }

    // 번데기 각자 카운트
    if (guho === 0) bunCnt++;
    if (guho === 1) degiCnt++;

    if ((isDegi === 1 && T === degiCnt) || (isDegi === 0 && T === bunCnt)) {
      return i;
    }

    i++;
    repeatCnt++;
  }
}

console.log(solution(A, T, isDegi));
