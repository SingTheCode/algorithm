const fs = require("fs");
const BOJkey = 1;
const input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, M] = input[0].split(" ").map((el) => +el);
const manjokList = input.slice(1).map((el) => el.split(" ").map((el) => +el));

function solution(N, M, manjokList) {
  let result = 0;

  function getCombinations(arr, selectNumbers) {
    const results = [];
    if (selectNumbers === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, selectNumbers - 1);
      const append = combinations.map((el) => [fixed, ...el]);
      results.push(...append);
    });
    return results;
  }

  // MC3 조합
  getCombinations(
    Array.from(new Array(M), (_, idx) => idx),
    3
  ).forEach((permutation) => {
    let tmpSum = 0;
    // permutation의 세 원소를 인덱스로 가지는 people의 치킨 만족도 중 가장 큰 값 더해
    manjokList.forEach((people) => {
      const tmp = permutation.map((value) => people[value]);
      tmpSum += Math.max(...tmp);
    });
    // 최댓값으로 교체
    result = Math.max(result, tmpSum);
  });

  return result;
}

console.log(solution(N, M, manjokList));
