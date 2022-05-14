const input = [
  "10 13",
  "BBBBBBBBWBWBW",
  "BBBBBBBBBWBWB",
  "BBBBBBBBWBWBW",
  "BBBBBBBBBWBWB",
  "BBBBBBBBWBWBW",
  "BBBBBBBBBWBWB",
  "BBBBBBBBWBWBW",
  "BBBBBBBBBWBWB",
  "WWWWWWWWWWBWB",
  "WWWWWWWWWWBWB",
];

const whiteFirst = [
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
];

const blackFirst = [
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
  "BWBWBWBW",
  "WBWBWBWB",
];

const NM = input
  .shift()
  .split(" ")
  .map((num) => parseInt(num));
const N = NM.shift();
const M = NM.shift();
const minArr = [];

function whiteFirstPaint(y, x) {
  let counter = 0;

  for (let i = y; i < y + 8; i++)
    for (let j = x; j < x + 8; j++)
      if (input[i][j] !== whiteFirst[i - y][j - x]) counter++;

  return counter;
}

function blackFirstPaint(y, x) {
  let counter = 0;

  for (let i = y; i < y + 8; i++)
    for (let j = x; j < x + 8; j++)
      if (input[i][j] !== blackFirst[i - y][j - x]) counter++;

  return counter;
}

for (let i = 0; i + 7 < N; i++)
  for (let j = 0; j + 7 < M; j++) {
    minArr.push(whiteFirstPaint(i, j));
    minArr.push(blackFirstPaint(i, j));
  }
console.log(Math.min.apply(null, minArr));

// input은 예제를 바로 넣어서 확인

// 흰색이 먼저, 검정색이 먼저 시작되는 케이스를 먼저 만든 후
// 입력 받은 값과 반복하여 비교한다

// 각 상황에서의 최솟값을 min 배열에 넣은 후 Math api를 이용해 최솟값을 찾는다

// 반복문에서 종료 시점을 i + 7 < N으로 해서 8 * 8 의 체스판이 input받은 MN의 행렬 크기를 넘어가지 않게끔 했다
