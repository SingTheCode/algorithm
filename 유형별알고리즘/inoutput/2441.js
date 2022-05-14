const input = ["5"];
let str = "";
for (let i = 0; i < parseInt(input[0]); i++) {
  for (let k = 0; k < i; k++) {
    str += " ";
  }
  for (let j = 0; j < parseInt(input[0]) - i; j++) {
    str += "*";
  }
  console.log(str);
  str = "";
}
