let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

input = input[0];

const solution = (input) => {
  let result = "";
  let tmp = "";
  let i = 0;
  let j = 0;

  while (i <= input.length) {
    console.log(input);
    if (i === input.length) {
      while (j < tmp.length) {
        result += tmp[tmp.length - 1 - j];
        j++;
      }
      tmp = "";
      i++;
      j = 0;
    } else if (input[i] === "<") {
      if (tmp !== "") {
        while (j < tmp.length) {
          result += tmp[tmp.length - 1 - j];
          j++;
        }
        tmp = "";
        j = 0;
      } else {
        while (input[i] !== ">") {
          result += input[i];
          i++;
        }
        result += input[i];
        i++;
      }
    } else if (input[i] === " ") {
      while (j < tmp.length) {
        result += tmp[tmp.length - 1 - j];
        j++;
      }
      result += input[i];
      tmp = "";
      i++;
      j = 0;
    } else {
      tmp += input[i];
      i++;
    }
  }
  return result;
};

console.log(solution(input));
