let fs = require("fs");
let BOJkey = 1;
let input = fs
  .readFileSync(BOJkey ? "./input.txt" : "/dev/stdin")
  .toString()
  .split("\n");

const [N, K] = input[0].split(" ").map((el) => +el);

function solution(N, K) {
  let result = 0;

  for (let hour = 0; hour < N + 1; hour++) {
    let hourTmp = "";

    if (hour < 10) {
      hourTmp = `0${hour}`;
    } else hourTmp = String(hour);

    let hourCheck = hourTmp.split("").find((value) => value === String(K));

    for (let min = 0; min < 60; min++) {
      let minTmp = "";

      if (min < 10) {
        minTmp = `0${min}`;
      } else minTmp = String(min);

      let minCheck = minTmp.split("").find((value) => value === String(K));

      for (let sec = 0; sec < 60; sec++) {
        let secTmp = "";

        if (sec < 10) {
          secTmp = `0${sec}`;
        } else secTmp = String(sec);

        let secCheck = secTmp.split("").find((value) => value === String(K));
        
        if (hourCheck || minCheck || secCheck) result++;
      }
    }
  }
  return result;
}

console.log(solution(N, K));
