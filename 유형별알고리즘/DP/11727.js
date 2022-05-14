const input = ["8"];

let dp = new Array(parseInt(input[0]) + 1).fill(0);
function solution(num) {
  if (num === 1) return 1;
  if (num === 2) return 3;
  if (dp[num] !== 0) return dp[num];
  dp[num] = (solution(num - 1) + solution(num - 2) * 2) % 10007;
  return dp[num];
}
console.log(solution(parseInt(input[0])));
