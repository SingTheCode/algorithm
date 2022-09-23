let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const n = Number(input[0]);
const k = Number(input[1]);
const numList = input.slice(2);

function solution(n, k, numList) {
  const numSet = new Set();

  function getPermutations(arr, selectNumbers) {
    const results = [];
    if (selectNumbers === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
      const rest = [...origin.slice(0, index), ...origin.slice(index + 1)];
      const permutations = getPermutations(rest, selectNumbers - 1);
      const attached = permutations.map((el) => [fixed, ...el]);
      results.push(...attached);
    });
    return results;
  }
  
  getPermutations(numList, k).forEach((permutation) => {
    numSet.add(permutation.join(""));
  });
  return numSet;
}

console.log(solution(n, k, numList).size);
