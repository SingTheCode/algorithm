const input = ["5", "20 10 35 30 7"];
const string = input[1].split(" ");
let numbers = [];
for (let i = 0; i < parseInt(input[0]); i++) {
  numbers.push(parseInt(string[i]));
}
let min = numbers[0];
let max = numbers[0];
for (let j = 0; j < numbers.length; j++) {
  if (min > numbers[j]) {
    min = numbers[j];
  }
  if (max < numbers[j]) {
    max = numbers[j];
  }
}
console.log(min, max);
