let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M] = input[0].split(" ").map((el) => +el);
const arr = input[1].split(" ").map((el) => +el);

const solution = (N, M, arr) => {
  let result = 3000000;
  let minGap = 3000000;
  // i, j, k로 삼중 반복
  for (let i = 0; i < N - 2; i++) {
    for (let j = i + 1; j < N - 1; j++) {
      for (let k = j + 1; k < N; k++) {
        // 값이 21보다 작고, 기존보다 차이가 작으면 교체
        const tmpGap = M - (arr[i] + arr[j] + arr[k]);
        if (tmpGap >= 0 && tmpGap < minGap) {
          minGap = tmpGap;
          result = arr[i] + arr[j] + arr[k];
        }
      }
    }
  }
  return result;
};

console.log(solution(N, M, arr));
