const input = ["3"];
let result = "";
for (let i = 0; i < parseInt(input[0]) - 1; i++) {
  for (let j = 0; j < parseInt(input[0]) - i - 1; j++) {
    result += " ";
  }
  result += "*";
  for (let k = 0; k < 2 * i - 1; k++) {
    result += " ";
  }
  if (i !== 0) {
    result += "*";
  }
  console.log(result);
  result = "";
}
for (let l = 0; l < parseInt(input[0]) * 2 - 1; l++) {
  result += "*";
}
console.log(result);
