let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M] = input[0].split(" ").map((el) => +el);
const DNAList = input.splice(1, N + 1);

function solution(N, M, DNAList) {
  let resultDNA = "";
  let sum = 0;

  for (let i = 0; i < M; i++) {
    // 알파벳 겹치는 횟수
    const sameCharCntList = new Array(26).fill(0);

    DNAList.forEach((DNA) => {
      const idx = DNA.charCodeAt(i) - 65;
      sameCharCntList[idx]++;
    });

    // 가장 큰 값 찾아
    const maxValue = Math.max(...sameCharCntList);
    const maxIdx = sameCharCntList.indexOf(maxValue);
    const maxChar = String.fromCharCode(maxIdx + 65);
    resultDNA += maxChar;
    sum += sameCharCntList.reduce((prev, cur, curIdx) => {
      if (curIdx !== maxIdx) {
        return prev + cur;
      }
      return prev;
    }, 0);
  }

  return `${resultDNA}\n${sum}`;
}

console.log(solution(N, M, DNAList));
