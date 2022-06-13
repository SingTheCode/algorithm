let V = 0;
let G = [];
let visited = [];

function solution(cities, roads, cars, customers) {
  let result = [];
  V = cities.length;
  G = Array.from(Array(V + 1), () => Array(V + 1).fill(0));
  visited = Array(V + 1).fill(0);

  for (let i = 0; i < roads.length; i++) {
    let tmp = roads[i].split(" ");
    G[cityToIndex(tmp[0])][cityToIndex(tmp[1])] = parseInt(tmp[2]);
    G[cityToIndex(tmp[1])][cityToIndex(tmp[0])] = parseInt(tmp[2]);
  }

  cars = cars.map((value) => {
    value = value.split(" ");
    return [value[0], parseInt(value[1]), parseInt(value[2])];
  });

  customers = customers.map((value) => {
    value = value.split(" ");
    return [value[0], value[1], parseInt(value[2])];
  });

  for (let customer of customers) {
    let minPrice = 1000000;
    let minCar = "";
    let positiveCars = cars.filter((car) => car[1] >= customer[2]);

    let startPrice = 1000000;
    let endPrice = 1000000;
    for (let car of positiveCars) {
      startPrice = DFS(
        cityToIndex(car[0]),
        cityToIndex(car[0]),
        cityToIndex(customer[0])
      );
      visited = Array(V + 1).fill(0);
      endPrice = DFS(
        cityToIndex(customer[0]),
        cityToIndex(customer[0]),
        cityToIndex(customer[1])
      );

      if (minPrice > startPrice + endPrice) {
        minPrice = startPrice + endPrice;
        minCar = car[0];
      }
    }
    result.push(minCar);
  }
  return result;
}

function cityToIndex(city) {
  return city.charCodeAt(0) - 96;
}

function DFS(sv, cv, ev) {
  let minPrice = 1000000;
  let price = 0;
  let stack = [sv];
  let pv = sv;

  while (stack.length > 0) {
    cv = stack.pop();

    if (cv === ev) {
      minPrice = Math.min(minPrice, price);
      price = 0;
      continue;
    }

    if (!visited[cv]) {
      visited[cv] = 1;
      price += G[pv][cv];

      for (let j = 0; j < V + 1; j++) {
        if (G[cv][j] > 0 && !visited[j]) {
          stack.push(j);
          pv = cv;
        }
      }
    }
  }
}

console.log(
  solution(
    ["a", "b", "c"],
    ["a b 1", "a c 1", "b c 1"],
    ["a 100 10", "b 300 20", "c 50 4"],
    ["a b 100", "a b 30", "c a 250"]
  )
);
