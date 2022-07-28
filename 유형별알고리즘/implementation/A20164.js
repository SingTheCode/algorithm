let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

let max = 0;
let min = 1000000;

// 각 자리수의 홀수 개수 확인
function getOdd(n) {
  let odd = 0;
  for (let i = 0; i < n.length; i++) {
    if (n[i] % 2 != 0) {
      odd += 1;
    }
  }
  return odd;
}

function solution(n, odd) {
  // 1자리수이면 홀수 개수의 min, max 업데이트(종료 조건)
  if (n.length === 1) {
    min = Math.min(min, odd);
    max = Math.max(max, odd);
  }
  // 2자리수이면
  else if (n.length === 2) {
    let temp = String(Number(n[0]) + Number(n[1]));
    solution(temp, odd + getOdd(temp));
  }
  // 3자리수 이상이면
  else {
    for (let i = 0; i < n.length - 2; i++) {
      for (let j = i + 1; j < n.length - 1; j++) {
        let a = n.slice(0, i + 1);
        let b = n.slice(i + 1, j + 1);
        let c = n.slice(j + 1);
        temp = String(Number(a) + Number(b) + Number(c));
        solution(temp, odd + getOdd(temp));
      }
    }
  }
}

solution(input[0], getOdd(input[0]));
console.log(min, max);
