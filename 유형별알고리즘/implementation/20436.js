let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

let [leftKey, rightKey] = input[0].split(" ");
input = input[1].split("");

function solution(leftKey, rightKey, input) {
  let result = 0;
  let keys = {
    q: [0, 0],
    w: [0, 1],
    e: [0, 2],
    r: [0, 3],
    t: [0, 4],
    y: [0, 5],
    u: [0, 6],
    i: [0, 7],
    o: [0, 8],
    p: [0, 9],
    a: [1, 0],
    s: [1, 1],
    d: [1, 2],
    f: [1, 3],
    g: [1, 4],
    h: [1, 5],
    j: [1, 6],
    k: [1, 7],
    l: [1, 8],
    z: [2, 0],
    x: [2, 1],
    c: [2, 2],
    v: [2, 3],
    b: [2, 4],
    n: [2, 5],
    m: [2, 6],
  };
  let left = [
    "q",
    "w",
    "e",
    "r",
    "t",
    "a",
    "s",
    "d",
    "f",
    "g",
    "z",
    "x",
    "c",
    "v",
  ];
  let right = ["y", "u", "i", "o", "p", "h", "j", "k", "l", "b", "n", "m"];

  function solve(key) {
    let tmp = 0;
    if (left.find((value) => value === key)) {
      tmp =
        Math.abs(keys[key][0] - keys[leftKey][0]) +
        Math.abs(keys[key][1] - keys[leftKey][1]);
      leftKey = key;
      result += tmp + 1;
      return;
    }

    if (right.find((value) => value === key)) {
      tmp =
        Math.abs(keys[key][0] - keys[rightKey][0]) +
        Math.abs(keys[key][1] - keys[rightKey][1]);
      rightKey = key;
      result += tmp + 1;
      return;
    }
  }

  input.forEach((key) => {
    solve(key);
  });

  return result;
}

console.log(solution(leftKey, rightKey, input));
