let fs = require("fs");
let input = fs.readFileSync("test").toString().split("\n");

const N = input[0].split(" ").map((el) => +el);
const data = [];
for (let i = 1; i < N[1] + 1; i++) {
  // 위에서 N과 info를 받을떄 input[0], input[1]이 빠져나갔기 때문에 2~N+1을 받아야한다.
  data.push(input[i].split(" ").map((el) => +el));
}

console.log(N, data);

class Node {
  constructor(data) {
    this.data = data;
    this.children = [];
  }

  add(data) {
    this.children.push(new Node(data));
  }

  remove(data) {
    this.children = this.children.filter((child) =>
      child.data === data ? false : true
    );
  }
}

class Tree {
  constructor() {
    this.root = null;
  }

  BFS(fn) {
    if (this.root === null) return;

    const unvisitedQueue = [this.root];
    while (unvisitedQueue.length !== 0) {
      const current = unvisitedQueue.shift();
      unvisitedQueue.push(...current.children);
      fn(current);
    }
  }

  DFS(fn) {
    if (this.root === null) return;

    const unvisitedList = [this.root];
    while (unvisitedList.length !== 0) {
      const current = unvisitedList.shift();
      unvisitedList.unshift(...current.children);
      fn(current);
    }
  }
}

const solution = (n) => {
  const lettersBFS = [];
  const lettersDFS = [];

  const B = new Tree();
  B.root = new Node(n[2]);
  B.root.add("b");
  B.root.add("c");
  B.root.children[0].add("d");

  B.BFS((node) => lettersBFS.push(node.data));
  B.DFS((node) => lettersDFS.push(node.data));

  console.log(lettersBFS);
  console.log(lettersDFS);
};

solution();
