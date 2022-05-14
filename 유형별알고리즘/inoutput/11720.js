const input = ["5", "54321"];
const num = input[1].split("");
let sum = 0;
for (let i = 0; i < parseInt(input[0]); i++) {
  sum += parseInt(num[i]);
}
console.log(sum);
