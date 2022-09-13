let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [a, b, c, d, e, f] = input[0].split(" ").map((el) => +el);

function solution(a, b, c, d, e, f) {
  let result = "";

  for (let i = -999; i < 1000; i++) {
    for (let j = -999; j < 1000; j++) {
      if (a * i + b * j === c && d * i + e * j === f) {
        result = `${i} ${j}`;
        return result;
      }
    }
  }
}

console.log(solution(a, b, c, d, e, f));
