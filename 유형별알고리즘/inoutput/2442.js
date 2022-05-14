const input = ["5"];
let str = "";
for (let i = 0; i < parseInt(input[0]); i++) {
  for (let j = parseInt(input[0]) - i - 1; j > 0; j--) {
    str += " ";
  }
  for (let k = 1; k < (i + 1) * 2; k++) {
    str += "*";
  }
  console.log(str);
  str = "";
}
