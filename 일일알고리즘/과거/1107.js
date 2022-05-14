let start = new Date();
const input = ["4999999", "4", "0 1 3 9"];
const missNum = input[2].split(" ");

let standard = parseInt(input[0]);

let min = [];
let curr = 0;
let prev = 0;

if (input[1] === "0") {
  if (standard === 99 || standard === 101) {
    console.log(1);
    return;
  }
  if (standard === 98 || standard === 102) {
    console.log(2);
    return;
  }
}
if (standard === 100) {
  console.log(0);
  return;
}

while (true) {
  const currArray = curr.toString().split("");
  const isNotInclude = currArray.some((value) => {
    for (let i = 0; i < missNum.length; i++) {
      if (value === missNum[i]) {
        return true;
      }
    }
  });

  if (isNotInclude) {
    curr++;
    continue;
  }

  if (curr > standard) {
    min.push(prev);
    min.push(curr);
    break;
  }
  prev = curr;
  curr++;
}

let approach = standard - min[0] > min[1] - standard ? min[1] : min[0];
let result = approach.toString().length + Math.abs(approach - standard);
result = result > Math.abs(standard - 100) ? Math.abs(standard - 100) : result;
console.log(result);

// 반례를 못 찾는 상황
