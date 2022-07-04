let fs = require("fs");
let input = fs.readFileSync("./input.txt").toString().split("\n");

const T = +input[0];
let line = 1;

function resultArray(arr, N, angle) {
  angle = parseInt(angle / 45);
  for (let tryCnt = 0; tryCnt < Math.abs(angle) + 1; tryCnt++) {
    console.log(parseInt(N / 2))
    for (let k = 1; k < parseInt(N / 2) + 1; k++) {
      console.log(2);

      // if (angle < 0) k = -k;
      let temp = arr[(parseInt(N / 2), parseInt(N / 2) - k)];
      arr[(parseInt(N / 2), parseInt(N / 2) - k)] =
        arr[(parseInt(N / 2) + k, parseInt(N / 2))];
      arr[(parseInt(N / 2) + k, parseInt(N / 2))] =
        arr[(parseInt(N / 2) + k, parseInt(N / 2) + k)];
      arr[(parseInt(N / 2) + k, parseInt(N / 2) + k)] =
        arr[(parseInt(N / 2), parseInt(N / 2) + k)];
      arr[(parseInt(N / 2), parseInt(N / 2) + k)] =
        arr[(parseInt(N / 2) - k, parseInt(N / 2) + k)];
      arr[(parseInt(N / 2) - k, parseInt(N / 2) + k)] =
        arr[(parseInt(N / 2) - k, parseInt(N / 2))];
      arr[(parseInt(N / 2) - k, parseInt(N / 2))] =
        arr[(parseInt(N / 2) - k, parseInt(N / 2) - k)];
      arr[(parseInt(N / 2) - k, parseInt(N / 2) - k)] = temp;
    }
  }
  return arr;
}

while (line < input.length) {
  let [N, angle] = input[line].split(" ").map((el) => +el);
  let arr = [];
  for (let i = line + 1; i < line + N + 1; i++) {
    arr.push(input[i].split(" ").map((el) => +el));
  }
  // console.log(arr, angle)
  console.log("------------", arr, resultArray(arr, N, angle));
  line += N + 1;
}
