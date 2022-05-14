const fs = require("fs");
let input = fs.readFileSync("stdin").toString().split("\n");

let test = input.map((value) => +value);
let arrResult = [];

arrResult.push(1);
arrResult.push(2);
arrResult.push(4);

for (let i = 3; i < 10; i++) {
  arrResult.push(arrResult[i - 3] + arrResult[i - 2] + arrResult[i - 1]);
}
for (let j = 1; j < test[0] + 1; j++) {
  console.log(arrResult[test[j] - 1]);
}
