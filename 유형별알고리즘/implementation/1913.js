let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = Number(input[0]);
const findValue = Number(input[1]);
const arr = new Array(N).fill(Array(N).fill(0));
const di = [-1, 0, 1, 0];
const dj = [0, 1, 0, -1];
let ci = parseInt(N / 2);
let cj = parseInt(N / 2);
let k = 0;
let value = 1;
let countTwo = 0;
let moveLength = 1;

// 2
while (value <= N * N) {
  let ni, nj;

  // 2-1
  if (countTwo === 2) {
    countTwo = 0;
    moveLength++;
  }

  // 2-2
  for (let p = 1; p < moveLength + 1; p++) {
    ni = ci + di[k] * p;
    nj = cj + dj[k] * p;
    if (ni >= 0 && nj >= 0 && ni < N && nj < N) {
      arr[ni][nj] = value;
    }
    console.log(arr);
  }

  // 2-3
  countTwo++;
  k++;
  if (k === 4) k = 0;
  ci = ni;
  cj = nj;
}
