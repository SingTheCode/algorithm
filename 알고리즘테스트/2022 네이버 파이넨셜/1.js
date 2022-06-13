function solution(recruits, s1, s2) {
  var answer = [];
  let e1 = 0;
  let e2 = 0;

  let period_min = 0;
  let period_max = -1;
  let score_min = 0;
  let score_max = -1;

  let answerTargetArray = [];

  // 최대 찾기
  for (let i = 0; i < recruits.length; i++) {
    if (recruits[i][0] > period_max) {
      period_max = recruits[i][0];
    }
    if (recruits[i][1] > score_max) {
      score_max = recruits[i][1];
    }
  }
  // 최소 찾기
  for (let i = 0; i < recruits.length; i++) {
    if (i == 0) {
      period_min = recruits[i][0];
      score_min = recruits[i][1];
      continue;
    }
    if (recruits[i][0] < period_min) {
      period_min = recruits[i][0];
    }
    if (recruits[i][1] < score_min) {
      score_min = recruits[i][1];
    }
  }
  // brute force
  for (let i = period_min; i <= period_max; i++) {
    for (let j = score_min; j <= score_max; j++) {
      e1 = i;
      e2 = j;

      // 분류 결과를 저장할 배열 선언. 이번에는 E, J, S 다한다.
      let recruitClassifications = [];

      for (let k = 0; k < recruits.length; k++) {
        const period = recruits[k][0];
        const score = recruits[k][1];
        // expert
        if (period >= e1 && score >= e2) {
          recruitClassifications.push("Expert");
        } else if (period >= s1 || score >= s2) {
          recruitClassifications.push("Senior");
        } else {
          recruitClassifications.push("Junior");
        }
      }

      // 각 숫자 구하기
      let juniorCount = 0;
      let seniorCount = 0;
      let expertCount = 0;

      for (let k = 0; k < recruitClassifications.length; k++) {
        if (recruitClassifications[k] === "Expert") {
          expertCount++;
        } else if (recruitClassifications[k] === "Senior") {
          seniorCount++;
        } else {
          juniorCount++;
        }
      }
      // 각 카운트 별로 조건을 만족하는 지 구하기
      // 조건을 만족한다면, 답이 될 수 있는 배열에 e1, e2저장하기. (answerTarget..)
      if (
        0 < expertCount &&
        expertCount < seniorCount &&
        seniorCount < juniorCount
      ) {
        let arr = [];
        arr.push(e1);
        arr.push(e2);
        answerTargetArray.push(arr);
      }
    }
  }

  let e1Pluse2Max = -1;
  let e1_max = -1;
  let e2_max = -1;
  for (let i = 0; i < answerTargetArray.length; i++) {
    // 지금까지 구한 최댓 값보다 크다면
    if (answerTargetArray[i][0] + answerTargetArray[i][1] > e1Pluse2Max) {
      e1_max = answerTargetArray[i][0];
      e2_max = answerTargetArray[i][1];
      e1Pluse2Max = answerTargetArray[i][0] + answerTargetArray[i][1];
    } else if (
      answerTargetArray[i][0] + answerTargetArray[i][1] ===
      e1Pluse2Max
    ) {
      if (answerTargetArray[i][0] > e1_max) {
        e1_max = answerTargetArray[i][0];
        e2_max = answerTargetArray[i][1];
      }
    }
  }

  answer.push(e1_max);
  answer.push(e2_max);

  return answer;
}
