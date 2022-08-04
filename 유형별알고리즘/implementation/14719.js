let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [H, W] = input[0].split(" ").map((el) => +el);
const arr = input[1].split(" ").map((el) => +el);

function solution(H, W, arr) {
  let maxLine = H;
  let cnt = 0;

  // maxLine이 0이 될 때까지 한줄씩 반복
  while (maxLine > 0) {
    let maxIndexs = [];

    // maxIdx랑 Line이 겹치는 경우
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === maxLine) maxIndexs.push(i);
    }

    // maxIdx를 오름차순 정렬 후
    maxIndexs.sort((a, b) => a - b);

    // 시작점 끝점 사이의 빈칸 계산
    // maxIdxs의 길이가 2이상일 때
    if (maxIndexs.length > 1) {
      let currentIdx = 0;
      let startIdx = maxIndexs[0];
      let endIdx = maxIndexs[1];

      // 시작점이 마지막 maxidx가 될 때까지 반복
      while (currentIdx < maxIndexs.length - 1) {
        cnt += endIdx - startIdx - 1;
        currentIdx += 1;
        startIdx = maxIndexs[currentIdx];
        endIdx = maxIndexs[currentIdx + 1];
      }
    }

    // maxIdx 1개씩 줄여
    maxIndexs.forEach((idx) => {
      arr[idx] -= 1;
    });

    // maxLine 1개 줄여
    maxLine -= 1;
  }

  return cnt;
}

console.log(solution(H, W, arr));
