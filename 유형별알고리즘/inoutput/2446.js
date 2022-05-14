const input = ["5"];
let number = Number(input);
let result = "";

for (let i = 0; i < number; i++) {
  if (i !== 0) {
    result += "\n";
  }
  for (let j = 0; j < i; j++) {
    result += " ";
  }
  for (let k = 0; k < number * 2 - (2 * i + 1); k++) {
    result += "*";
  }
}

for (let i = 1; i < number; i++) {
  if (i !== number) {
    result += "\n";
  }
  for (let j = 1; j < number - i; j++) {
    result += " ";
  }
  for (let k = 0; k < 2 * i + 1; k++) {
    result += "*";
  }
}

console.log(result);
