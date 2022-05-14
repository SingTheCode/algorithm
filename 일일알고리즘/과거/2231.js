const fs = require("fs");
let input = fs.readFileSync("stdin").toString();

let result = 1;

while (true) {
  let value = result.toString().split("");
  let sum = value.reduce((prev, curr) => Number(prev) + Number(curr), 0);
  if (Number(input) === result + sum) {
    console.log(result.toString());
    break;
  }
  if (Number(input) < result) {
    console.log("0");
    break;
  }
  result++;
}
