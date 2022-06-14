let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const temp = [];
for (let i = 0; i < 5; i++) {
  temp.push(input[i]);
}
let inputArr = [];
for (let i = 5; i < 10; i++) {
  inputArr.push(input[i]);
}
const arr = inputArr.map((line) => line.split(" ").map((el) => +el));
const visited = new Array(5).fill(Array(5).fill(0));

// 1
for (let i = 0; i < 5; i++) {
  arr[i].findIndex(value => value)
}
console.log(arr);
