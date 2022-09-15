let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, KLength] = input[0].split(" ").map((el) => +el);
const K = input[1].split(" ").map((el) => +el);

function solution(N, K, KLength) {
  const KList = [];
  const regExp = /[1-9]/;
  K = K.sort((a, b) => a - b);

  // K원소들로 만들 수 있는 값을 오름차순으로 추가
  function makeKList(idx, str) {
    if (idx === String(N).length) {
      KList.push(Number(str));
      return;
    }

    if (!regExp.test(str)) {
      makeKList(idx + 1, String(str) + "0");
    }

    for (let i = 0; i < KLength; i++) {
      makeKList(idx + 1, String(str) + String(K[i]));
    }
  }
  makeKList(0, "");
  KList.shift();

  // KList중에 가장 큰 값부터 작은 값 순으로 N보다 작거나 같은 값 탐색
  for (let i = KList.length - 1; i >= 0; i--) {
    if (KList[i] <= N) {
      return KList[i];
    }
  }
}

console.log(solution(N, K, KLength));
