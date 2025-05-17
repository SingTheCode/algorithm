const file = `6
4
2 3
3 4
4 5
5 1`;

const input = file.split("\n");

const nodeCount = Number(input[0]);
const pathList = input.slice(2).map((item) => item.split(" ").map(Number));
const visited = new Array(nodeCount).fill(false);

dfs(1); // 오직 시작점 1에서만 시작

function dfs(current) {
  if (visited[current - 1]) return;
  visited[current - 1] = true;

  pathList.forEach(([a, b]) => {
    if (a === current) dfs(b);
    else if (b === current) dfs(a);
  });
}

const result = visited.filter(Boolean);
console.log(result.length - 1); // 1번 컴퓨터 제외
