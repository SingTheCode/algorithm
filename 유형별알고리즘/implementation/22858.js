let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, K] = input[0].split(" ").map((el) => +el);
let P = [0, ...input[1].split(" ").map((el) => +el)];
let D = [0, ...input[2].split(" ").map((el) => +el)];

function solution(N, K, D, P) {
  let result = "";

  function action(D, P) {
    let tmp = [...P];
    for (let j = 1; j < N + 1; j++) {
      P[D[j]] = tmp[j];
    }
  }
  for (let i = 0; i < K; i++) {
    action(D, P);
  }
  P.shift();
  result = P.join(" ");
  return result;
}

console.log(solution(N, K, D, P));
