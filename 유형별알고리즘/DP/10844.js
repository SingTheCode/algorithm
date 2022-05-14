const input = ["2"];
let sum = 0;
let result = 9;
const N = parseInt(input[0]);
let dp = new Array(N);
for (let i = 0; i < N; i++) {
  dp[i] = new Array(10).fill(0);
}

function solution(n) {
  let temp = new Array(10);
  if (n === 1) {
    for (let i = 1; i < 10; i++) temp[i] = 1;
  } else {
    dp[n - 1] = solution(n - 1);
    temp[0] = dp[n - 1][1];
    temp[9] = dp[n - 1][8];
    for (let i = 1; i < 9; i++) {
      temp[i] = (dp[n - 1][i - 1] + dp[n - 1][i + 1]) % 1000000000;
    }
  }
  return temp;
}

solution(N);
console.log(dp);
if (N > 1) {
  for (let i = 0; i < 10; i++) {
    sum += dp[N - 1][i];
  }
  console.log(sum);
  result = (sum * 2 - dp[N - 1][0] - dp[N - 1][9]) % 1000000000;
}
console.log(result);
