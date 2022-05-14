const input = ["5"];
let str = "";
for (let i = 1; i < parseInt(input[0]) + 1; i++) {
  for (let k = 0; k < parseInt(input[0]) - i; k++) {
    str += " ";
  }
  for (let j = 0; j < i; j++) {
    str += "*";
  }
  console.log(str);
  str = "";
}
