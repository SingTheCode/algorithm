let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

function solution(input) {
  input = input.split("");
  let ducks = [];
  let ducksLastChar = [];
  let result = 0;

  // 입력받은 문자에 대한 로직을 실행한다.
  function checkDuck(char) {
    // 입력받은 문자가 q일 경우 집어넣는다.
    if (char === "q") {
      ducks.push("q");
      ducksLastChar.push("q");
      // 새로운 오리가 추가될 때마다, 현재 오리의 마리 수를 최대 마리 수와 비교한다.
      return 1;
    }

    // ducks의 마지막 문자가 현재 입력받은 문자의 전 문자인 경우를 찾아 집어넣는다.
    for (let i = 0; i < ducks.length; i++) {
      if (ducksLastChar[i] === findNeedChar(char)) {
        ducks[i] += char;
        ducksLastChar[i] = char;
        // 현재 입력받은 문자가 k인 경우, 마지막문자가 c인 문자를 뺀다.
        if (char === "k") {
          ducks.splice(i, 1);
          ducksLastChar.splice(i, 1);
          result
        }
        return 1;
      }
    }
    result = -1;
    return -1;
  }

  function findNeedChar(char) {
    if (char === "u") return "q";
    if (char === "a") return "u";
    if (char === "c") return "a";
    if (char === "k") return "c";
  }

  input.forEach((char) => {
    if (checkDuck(char) === -1) return result;
  });

  // if (ducks.length !== 0) result = -1;

  return result;
}

console.log(solution(input[0]));
