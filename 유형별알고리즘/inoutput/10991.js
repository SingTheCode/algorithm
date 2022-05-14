const input = ["2"];
let result = "";
for (let i = 0; i < parseInt(input[0]); i++) {
  for (let j = 0; j < parseInt(input[0]) - i - 1; j++) {
    result += " ";
  }
  for (let k = 0; k < i + 1; k++) {
    result += "*";
    result += " ";
  }
  console.log(result);
  result = "";
}
