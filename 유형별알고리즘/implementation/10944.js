let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const n = Number(input[0]);

function solution(n) {
  let top = 3;
  let arr = ["*"];
  let result = "";

  function solve(n) {
    if (n === 1) return arr;
    for (let i = 2; i < n + 1; i++) {
      for (let j = 0; j < (i - 2) * 4 + 1; j++) {
        arr[j] = "* " + arr[j] + " *";
      }
      arr.unshift("*" + " ".repeat((i - 2) * 4 + 3) + "*");
      arr.unshift("*".repeat((i - 2) * 4 + 5));
      arr.push("*" + " ".repeat((i - 2) * 4 + 3) + "*");
      arr.push("*".repeat((i - 2) * 4 + 5));
    }
  }

  function print() {
    for (let i = 0; i < arr.length; i++) {
      result = arr.join("\n");
    }
  }

  solve(n);
  print();
  return result;
}

console.log(solution(n));
