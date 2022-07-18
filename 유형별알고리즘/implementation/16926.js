let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M, R] = input[0].split(" ").map((el) => +el);
let arr = [];

for (let i = 1; i < input.length; i++) {
  arr.push(input[i].split(" ").map((el) => +el));
}

function solution(N, M, R, arr) {
  let result = "";

  function rotate() {
    let tmp = arr.map((v) => [...v]);

    for (let i = 0; i < N; i++) {
      for (let j = 0; j < M; j++) {
        if (i === j) {
          if (i < N / 2) {
            arr[i][j] = tmp[i][j + 1];
          } else if (i >= N / 2) {
            arr[i][j] = tmp[i][j - 1];
          }
        } else if (i + j === N - 1) {
          if (i >= N / 2) {
            arr[i][j] = tmp[i - 1][j];
          } else if (i < N / 2) {
            arr[i][j] = tmp[i + 1][j];
          }
        } else if (i < N / 2 && j > 0 && j < M - 1) {
          arr[i][j] = tmp[i][j + 1];
        } else if (i > N / 2 && j > 0 && j < M - 1) {
          arr[i][j] = tmp[i][j - 1];
        } else if (i > 0 && i < N - 1 && j > M / 2) {
          arr[i][j] = tmp[i + 1][j];
        } else if (i > 0 && i < N - 1 && j < M / 2) {
          arr[i][j] = tmp[i - 1][j];
        }
      }
    }
  }

  for (let k = 0; k < R; k++) {
    rotate();
    console.log("---------");
    console.log(arr);
  }
  result = arr.reduce((acc, cur) => acc + cur.join(" ") + "\n", "");
  return result;
}

console.log(solution(N, M, R, arr));
