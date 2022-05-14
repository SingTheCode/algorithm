function solution() {
  for (let a = 1; a < 100; a++) {
    for (let b = 2; b < a; b++) {
      for (let c = b; c <= a; c++) {
        for (let d = c; d <= a; d++) {
          if (a ** 3 === b ** 3 + c ** 3 + d ** 3) {
            console.log(`Cube = ${a}, Triple = (${b}, ${c}, ${d})`);
          }
        }
      }
    }
  }
}
solution();

// 처음부터 끝까지 전부 돌려본다

// 반복문이 많이 중첩되고 신경쓰지 않는다
