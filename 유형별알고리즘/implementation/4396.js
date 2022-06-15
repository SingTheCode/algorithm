let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const N = Number(input[0]);
const mine = [];
const open = [];
let arr = [];
let result = "";

function solution() {
  // 1 & 2
  for (let i = 1; i < N + 1; i++) {
    mine.push(input[i].split(""));
    open.push(input[N + i].split(""));
    arr.push(Array(N).fill("."));
  }

  // 4
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      // 4-1
      if (open[i][j] === "x") {
        let tmp = findMine(i, j);

        // 4-2
        if (tmp === -1) {
          for (let p = 0; p < N; p++) {
            for (let q = 0; q < N; q++) {
              if (mine[p][q] === "*") arr[p][q] = "*";
            }
          }
        }

        // 4-3
        else {
          arr[i][j] = tmp;
        }
      }
    }
  }
  arr = arr.map((line) => line.join(""));
  result = arr.join("\n");
  return result;
}

// 3
function findMine(ci, cj) {
  const di = [-1, -1, 0, 1, 1, 1, 0, -1];
  const dj = [0, 1, 1, 1, 0, -1, -1, -1];
  let cnt = 0;

  // 3-1
  if (mine[ci][cj] === "*") return -1;

  // 3-2
  for (let k = 0; k < 8; k++) {
    let ni = ci + di[k];
    let nj = cj + dj[k];

    if (ni >= 0 && ni < N && nj >= 0 && nj < N) {
      if (mine[ni][nj] === "*") cnt++;
    }
  }
  return cnt;
}

console.log(solution());
