const input = ["3"];
let str = "";
for (let i = 0; i < parseInt(input[0]); i++) {
  for (let j = 0; j < parseInt(input[0]) - i - 1; j++) {
    str += " ";
  }
  for (let k = 0; k < i + 1; k++) {
    str += "*";
  }
  console.log(str);
  str = "";
}

for (let i = 0; i < parseInt(input[0]) - 1; i++) {
  for (let k = 0; k < i + 1; k++) {
    str += " ";
  }
  for (let j = 0; j < parseInt(input[0]) - i - 1; j++) {
    str += "*";
  }
  console.log(str);
  str = "";
}
