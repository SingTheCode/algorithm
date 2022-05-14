const input = ["1 1", "2 3", "3 4", "9 8", "9 9"];
let a,
  b = 0;
for (let i = 0; i < input.length; i++) {
  [a, b] = input[i].split(" ");
  console.log(parseInt(a) + parseInt(b));
}
