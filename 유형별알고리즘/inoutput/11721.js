let input = ["BaekjoonOnlineJudge"];
input.push("");
const str = input[0].split("");
let cnt = 0;
let result = "";
for (let i = 0; i < str.length; i++) {
  result += str[i];
  cnt++;
  if (cnt === 10) {
    console.log(result);
    result = "";
    cnt = 0;
  }
  if (i === str.length - 1) {
    console.log(result);
  }
}
