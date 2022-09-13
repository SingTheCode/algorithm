let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [A, B, C, M] = input[0].split(" ").map((el) => +el);

function solution(A, B, C, M) {
  let piro = 0;
  let work = 0;

  for (let i = 0; i < 24; i++) {
    if (piro + A > M) {
      piro -= C;
      if (piro < 0) piro = 0;
      continue;
    }
    piro += A;
    work += B;
  }
  return work;
}

console.log(solution(A, B, C, M));
