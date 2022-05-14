const input = ["9"];
let dp = new Array(1000);
function solution(n) {
  if (n === 0) return 0;
  if (n === 1) return 1;
  // n == 2일 때 추가
  if (n === 2) return 2;
  if (dp[n] !== undefined) return dp[n];
  dp[n] = (solution(n - 1) + solution(n - 2)) % 10007;
  return dp[n];
}
console.log(solution(parseInt(input[0])));
