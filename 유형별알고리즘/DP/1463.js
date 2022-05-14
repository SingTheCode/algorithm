const input = ["10"];
let result = 0;
// Top-Down
const Max = 1000000;
let dp = new Array(Max);
function solution(x) {
  if (x === 1) return 0;
  if (dp[x] !== undefined) return dp[x];

  let result = solution(x - 1) + 1;
  if (x % 3 === 0) result = Math.min(result, solution(x / 3) + 1);
  if (x % 2 === 0) result = Math.min(result, solution(x / 2) + 1);
  dp[x] = result;
  return result;
}
console.log(solution(parseInt(input[0])));

//Bottom-Up
// const Max = 1000000;
// let dp = new Array(Max);
// dp[1] = 0;
// for (let i = 1; i < x; i++) {
//   dp[i + 1] = Math.min(dp[i + 1], dp[i] + 1);
//   if (i * 2 < x) dp[i * 2] = Math.min(dp[i * 2], dp[i] + 1);
//   if (i * 3 < x) dp[i * 3] = Math.min(dp[i * 3], dp[i] + 1);
//     ;
// }
// console.log(dp[x]);
