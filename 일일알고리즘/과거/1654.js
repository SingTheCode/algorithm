const input = ["1 1", "3"];
let [k, n] = input[0].split(" ");
let kLan = [];
let count = [];

k = parseInt(k);
n = parseInt(n);
if (k === n && k === 1) {
  console.log(parseInt(input[1]));
  return 0;
}
for (let i = 1; i < Number(k) + 1; i++) {
  kLan.push(Number(input[i]));
}
kLan = kLan.sort((a, b) => a - b);

let left = 0;
let right = kLan[0];
while (true) {
  count = [];
  let mid = parseInt((left + right) / 2);

  for (let i = 0; i < kLan.length; i++) {
    count.push(parseInt(parseInt(kLan[i]) / mid));
  }
  let sum = count.reduce((sum, cnt) => sum + cnt, 0);
  if (sum === n) {
    for (let j = mid; j < right; j++) {
      count = [];
      current = j;
      for (let l = 0; l < kLan.length; l++) {
        count.push(parseInt(parseInt(kLan[l]) / j));
      }
      sum = count.reduce((sum, cnt) => sum + cnt, 0);
      if (sum < n) {
        console.log(current - 1);
        return 0;
      }
      if (mid === 1) {
        console.log(1);
        return 0;
      }
    }
  }
  if (sum < n) {
    right = mid - 1;
  }
  if (sum > n) {
    left = mid + 1;
  }
  if (left <= right) {
    console.log(0);
    return 0;
  }
}
