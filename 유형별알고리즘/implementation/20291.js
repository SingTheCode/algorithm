let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const N = Number(input[0]);
let arr = [];
for (let i = 1; i < N + 1; i++) {
  arr.push(input[i].split("."));
}

function solution(N, arr) {
  let resultObj = {};
  let result = [];

  arr.forEach((value) => {
    if (value[1] in resultObj) resultObj[value[1]]++;
    else resultObj[value[1]] = 1;
  });

  result = Object.entries(resultObj);
  result = result.sort((a, b) => {
    if (a[0] > b[0]) return 1;
    else return -1;
  });

  result = result.map((value) => {
    let temp = value[0] + " " + value[1];
    return temp;
  });
  result = result.join("\n");
  return result;
}

console.log(solution(N, arr));
