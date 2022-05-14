const fs = require("fs");
const input = fs.readFileSync("stdin.txt").toString().split("\n");
let value = input[1].split(" ");
const cnt = Number(input[0]);

function divisionTwo(value, i) {
  if (value[0] % i === 0 && value[1] % i === 0) {
    console.log(i);
  }
}

function divisionThree(value, i) {
  if (value[0] % i === 0 && value[1] % i === 0 && value[2] % i === 0) {
    console.log(i);
  }
}

value.sort((a, b) => b - a);
let minDivisor = value[cnt - 1];

if (cnt === 2) {
  for (let i = 1; i <= minDivisor / 2 + 1; i++) {
    divisionTwo(value, i);
  }
  divisionTwo(value, Number(minDivisor));
}

if (cnt === 3) {
  for (let i = 1; i <= minDivisor / 2 + 1; i++) {
    divisionThree(value, i);
  }
  divisionThree(value, Number(minDivisor));
}

// 반례를 못찾는 상황
