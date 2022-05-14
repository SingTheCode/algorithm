const input = ["1 1", "2 3", "3 4", "9 8", "5 2", "0 0"];
let a,
  b = 0;
for (let i = 0; i < input.length - 1; i++) {
  [a, b] = input[i].split(" ");
  console.log(parseInt(a) + parseInt(b));
}
