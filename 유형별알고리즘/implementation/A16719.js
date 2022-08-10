let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

function solution(input) {
  input = input.split("");
  let result = "";
  const check = Array.from(Array(input.length), (el) => false);

  function DFS(left, right) {
    // 왼쪽 기준 인덱스가 오른쪽 기준 인덱스보다 크면 종료
    if (left > right) return;

    let index = left;
    // 왼쪽 기준부터 오른쪽 기준까지 배열 중 가장 작은 단어와 그 인덱스 찾아
    for (let i = left; i < right + 1; i++) {
      if (input[index] > input[i]) index = i;
    }

    // 방문 체크
    check[index] = true;

    // 단어 한줄 완성
    for (let i = 0; i < input.length; i++) {
      if (check[i] === true) result += input[i];
    }
    result += "\n";

    // 재귀 호출
    // 기준 오른쪽부터 방문
    DFS(index + 1, right);
    DFS(left, index - 1);
  }
  DFS(0, input.length - 1);
  return result;
}

console.log(solution(input[0]));
