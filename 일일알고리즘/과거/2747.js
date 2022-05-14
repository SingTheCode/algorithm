const fs = require("fs");
const input = Number(fs.readFileSync("stdin").toString());

function solution(n) {
  let cnt = 0;
  let arrNum = [];

  while (cnt < n + 1) {
    if (cnt === 0) {
      arrNum.push(0);
      cnt++;
    }

    if (cnt === 1) {
      arrNum.push(1);
      cnt++;
    }

    arrNum.push(arrNum[cnt - 2] + arrNum[cnt - 1]);
    cnt++;
  }

  const result = arrNum.pop();
  return result;
}

console.log(solution(input));
