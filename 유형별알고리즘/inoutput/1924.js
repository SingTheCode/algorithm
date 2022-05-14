// 틀림
const input = ["7 18"];
let [m, d] = input[0].split(" ");
let day = [];
let sum = 0;
m = parseInt(m);
d = parseInt(d);

for (let i = 1; i < 13; i++) {
  if (i === 1) {
    day.push(0);
    continue;
  }
  if (i === 3) {
    day.push(28);
    continue;
  }
  if (i === 5 || i === 7 || i === 10 || i === 12) {
    day.push(30);
    continue;
  }
  day.push(31);
}
for (let j = 0; j < m; j++) {
  sum += day[j];
}
sum += d;
switch (sum % 7) {
  case 0:
    console.log("SUN");
    break;
  case 1:
    console.log("MON");
    break;
  case 2:
    console.log("TUE");
    break;
  case 3:
    console.log("WED");
    break;
  case 4:
    console.log("THU");
    break;
  case 5:
    console.log("FRI");
    break;
  case 6:
    console.log("SAT");
    break;
}
